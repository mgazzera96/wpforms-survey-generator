#!/usr/bin/env python3
"""
WPForms Survey Converter
Convierte documentos DOCX con encuestas a formato JSON de WPForms
"""

import json
import sys
import re
from pathlib import Path
from docx import Document


class SurveyConverter:
    """Convertidor de encuestas DOCX a JSON de WPForms"""
    
    def __init__(self, docx_path):
        """Inicializa el convertidor con un archivo DOCX"""
        self.doc = Document(docx_path)
        self.questions = []
        self.current_chapter = None
        
    def parse_document(self):
        """Parsea el documento completo"""
        lines = []
        for paragraph in self.doc.paragraphs:
            if paragraph.text.strip():
                lines.append(paragraph.text.strip())
        
        i = 0
        while i < len(lines):
            line = lines[i]
            
            # Detectar capítulo (español o inglés)
            if '📑 Capítulo' in line or 'Capítulo' in line.lower() or 'CHAPTER' in line.upper():
                self.current_chapter = self._extract_chapter_number(line)
                i += 1
                continue
            
            # Detectar pregunta
            if self._is_question(line):
                question_data = self._parse_question(lines, i)
                if question_data:
                    self.questions.append(question_data)
                    i = question_data['end_index']
                else:
                    i += 1
            else:
                i += 1
    
    def _extract_chapter_number(self, line):
        """Extrae el número del capítulo"""
        # Intentar con "Capítulo" (español)
        match = re.search(r'Capítulo\s+(\d+)', line, re.IGNORECASE)
        if match:
            return int(match.group(1))
        # Intentar con "CHAPTER" (inglés)
        match = re.search(r'CHAPTER\s+(\d+)', line, re.IGNORECASE)
        if match:
            return int(match.group(1))
        return 0
    
    def _is_question(self, line):
        """Determina si una línea es una pregunta"""
        # Detectar Q1. o Q1.1 formato
        return bool(re.match(r'^[PQ]\d+\.(\d+\s|\s)', line))
    
    def _parse_question(self, lines, start_index):
        """Parsea una pregunta completa"""
        question_line = lines[start_index]

        # Extraer número y tipo de pregunta - soportar Q1. y Q1.1 formato
        match = re.match(r'^[PQ](\d+(?:\.\d+)?)\.?\s+(.*?)(?:\s*→\s*(.*))?$', question_line)
        if not match:
            return None

        q_num = match.group(1)
        q_text = match.group(2)
        q_type_raw = match.group(3) if match.group(3) else ""

        # Si no hay tipo en la línea de pregunta, revisar la siguiente línea
        options_start_index = start_index + 1
        if not q_type_raw and options_start_index < len(lines):
            next_line = lines[options_start_index]
            # Buscar tipo entre paréntesis en la siguiente línea
            if next_line.startswith('(') and next_line.endswith(')'):
                q_type_raw = next_line.strip('()')
                options_start_index += 1  # Saltar esta línea para opciones

        # Determinar tipo de campo
        field_type, required, limit = self._determine_field_type(q_type_raw)

        # Recolectar opciones
        options = []
        i = options_start_index
        
        # Para Likert Scale, buscar columnas y filas
        if field_type == 'likert_scale':
            columns = []
            rows = []
            
            while i < len(lines):
                line = lines[i]
                
                if 'Columnas' in line or 'columnas' in line:
                    # Extraer columnas
                    col_text = line.split(':', 1)[1] if ':' in line else ''
                    columns = [c.strip() for c in re.split(r'[/|]', col_text) if c.strip()]
                    i += 1
                elif 'Filas' in line or 'filas' in line:
                    i += 1
                    # Recolectar filas
                    while i < len(lines) and not self._is_question(lines[i]) and 'Capítulo' not in lines[i]:
                        if lines[i] and not lines[i].startswith('Columnas'):
                            rows.append(lines[i].strip('- '))
                        i += 1
                    break
                else:
                    i += 1
                    if self._is_question(line) or 'Capítulo' in line:
                        break
            
            return {
                'number': q_num,
                'text': q_text,
                'type': field_type,
                'required': required,
                'columns': columns,
                'rows': rows,
                'end_index': i
            }
        
        # Para otros tipos, recolectar opciones normales
        while i < len(lines):
            line = lines[i]
            
            # Detener si encontramos otra pregunta o capítulo
            if self._is_question(line) or 'Capítulo' in line:
                break
            
            # Agregar opción si no está vacía
            if line and not line.startswith('Pregunta'):
                options.append(line.strip('- '))
            
            i += 1
        
        return {
            'number': q_num,
            'text': q_text,
            'type': field_type,
            'required': required,
            'limit': limit,
            'options': options,
            'end_index': i
        }
    
    def _determine_field_type(self, type_string):
        """Determina el tipo de campo WPForms basado en el string del documento"""
        type_lower = type_string.lower()
        required = '1' if 'required' in type_lower else '0'
        limit = None

        # Extraer límite si existe
        limit_match = re.search(r'máx\.?\s*(\d+)', type_lower)
        if limit_match:
            limit = limit_match.group(1)

        # Determinar tipo
        # Checkbox / Multiple choice
        if 'multiple choice' in type_lower or 'respuesta múltiple' in type_lower or 'checkbox' in type_lower:
            return 'checkbox', required, limit
        # Radio / Single choice
        elif 'single choice' in type_lower or 'opción única' in type_lower:
            return 'radio', required, None
        # Likert Scale
        elif 'likert' in type_lower:
            return 'likert_scale', required, None
        # Text fields
        elif 'text' in type_lower or 'open' in type_lower or 'abierta' in type_lower:
            return 'text', required, None
        else:
            # Default a radio si no se puede determinar
            return 'radio', required, None
    
    def to_wpforms_json(self, form_title="Encuesta", form_id="survey"):
        """Convierte las preguntas parseadas a formato JSON de WPForms"""
        fields = {}

        field_id_counter = 1
        for q in self.questions:
            # Saltar el ID 9 (reservado por WPForms)
            if field_id_counter == 9:
                field_id_counter = 10

            field_id = str(field_id_counter)

            field = {
                "id": field_id,
                "type": q['type'],
                "label": f"Q{q['number']} {q['text']}",
                "required": q['required']
            }

            field_id_counter += 1
            
            # Agregar opciones según el tipo
            if q['type'] in ['radio', 'checkbox']:
                choices = {}
                for i, option in enumerate(q.get('options', []), 1):
                    choices[str(i)] = {"label": option}
                field['choices'] = choices
                
                # Agregar límite si existe
                if q.get('limit'):
                    field['choice_limit'] = q['limit']
            
            elif q['type'] == 'likert_scale':
                field['columns'] = q.get('columns', [])
                field['rows'] = q.get('rows', [])
                field['single_row'] = '0'
            
            fields[field_id] = field
        
        # Estructura final
        return [{
            "id": form_id,
            "fields": fields,
            "settings": {
                "form_title": form_title,
                "submit_text": "Enviar",
                "form_class": form_id.replace('_', '-')
            }
        }]


def main():
    """Función principal"""
    if len(sys.argv) < 2:
        print("Uso: python3 convert_survey.py archivo.docx [salida.json]")
        print("\nEjemplo:")
        print("  python3 convert_survey.py 'Encuesta.docx' 'encuesta.json'")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else input_file.replace('.docx', '.json')
    
    # Verificar que el archivo existe
    if not Path(input_file).exists():
        print(f"Error: No se encuentra el archivo '{input_file}'")
        sys.exit(1)
    
    try:
        # Convertir
        print(f"📖 Leyendo: {input_file}")
        converter = SurveyConverter(input_file)
        
        print("🔄 Parseando documento...")
        converter.parse_document()
        
        print(f"✅ Encontradas {len(converter.questions)} preguntas")
        
        # Generar JSON
        form_title = Path(input_file).stem.replace('-', ' ').replace('_', ' ').title()
        form_id = Path(input_file).stem.lower().replace(' ', '_').replace('-', '_')
        
        json_data = converter.to_wpforms_json(form_title, form_id)
        
        # Guardar JSON
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(json_data, f, ensure_ascii=False, indent=2)
        
        print(f"💾 Guardado: {output_file}")
        print(f"📊 Total campos: {len(json_data[0]['fields'])}")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
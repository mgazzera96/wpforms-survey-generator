# 📋 WPForms Survey JSON Generator

## 📖 Descripción

Este proyecto convierte documentos de Word (.docx) con cuestionarios/encuestas a formato JSON compatible con WPForms para importación directa en WordPress.

## 🚀 Características

- ✅ Convierte documentos DOCX a JSON de WPForms
- ✅ Soporta múltiples tipos de preguntas
- ✅ Mantiene la estructura y numeración original
- ✅ Genera JSONs listos para importar

## 📁 Estructura del Proyecto

```
wpforms-survey-generator/
│
├── README.md                    # Este archivo
├── convert_survey.py           # Script de conversión
├── examples/                   # Ejemplos de JSONs generados
│   ├── coca-cola-survey.json
│   └── heineken-00-survey.json
└── docs/                       # Documentación adicional
    └── field-types.md         # Tipos de campos soportados
```

## 🛠️ Instalación

### Requisitos Previos

1. **Python 3.x** instalado
2. **Homebrew** (para macOS)

### Instalación de Dependencias

```bash
# Instalar Python con Homebrew (macOS)
brew install python

# Instalar la librería python-docx
pip3 install --break-system-packages --user python-docx
```

## 📊 Tipos de Campos Soportados

### 1. **Radio (Opción Única)**
```json
{
  "type": "radio",
  "label": "Pregunta de ejemplo",
  "required": "1",
  "choices": {
    "1": {"label": "Opción 1"},
    "2": {"label": "Opción 2"}
  }
}
```

### 2. **Checkbox (Opción Múltiple)**
```json
{
  "type": "checkbox",
  "label": "Seleccione todas las que apliquen",
  "required": "1",
  "choice_limit": "3",  // Opcional: límite máximo
  "choices": {
    "1": {"label": "Opción A"},
    "2": {"label": "Opción B"}
  }
}
```

### 3. **Likert Scale (Escala de Likert)**
```json
{
  "type": "likert_scale",
  "label": "Evalúe los siguientes aspectos",
  "required": "1",
  "columns": ["Muy malo", "Malo", "Regular", "Bueno", "Muy bueno"],
  "rows": ["Aspecto 1", "Aspecto 2", "Aspecto 3"],
  "single_row": "0"
}
```

### 4. **Text (Campo de Texto)**
```json
{
  "type": "text",
  "label": "Comentarios adicionales",
  "required": "1"
}
```

## 📝 Formato del Documento Word

El documento DOCX debe seguir este formato:

```
📑 Capítulo 0 - Título del Capítulo
Q1. Pregunta → Multiple Choice (required)
- Opción 1
- Opción 2
- Opción 3

Q2. Pregunta → Checkbox (máx. 3, required)
- Opción A
- Opción B
- Opción C

Q3. Pregunta → Likert Scale
Columnas: Mucho | Poco | Nada
Filas:
- Item 1
- Item 2

Q4. Pregunta abierta → Single Line Text (open)
```

## 🔄 Proceso de Conversión

### Método 1: Manual con Python

```bash
# Navegar a la carpeta del proyecto
cd ~/Downloads/wpforms-survey-generator

# Ejecutar el script de conversión
python3 convert_survey.py "archivo.docx" "salida.json"
```

### Método 2: Usando Claude CLI

```bash
# Comando básico
claude "Convierte el archivo archivo.docx a JSON de WPForms"

# Con guardar la conversación
claude --save nombre-encuesta.json "Lee el archivo ~/Downloads/archivo.docx y genera el JSON para WPForms"
```

## 📋 Ejemplos de Uso

### Ejemplo 1: Encuesta Coca-Cola (70 preguntas)

```bash
# Leer y convertir
python3 -c "
from docx import Document
import json

doc = Document('Tipos de preguntas (1).docx')
# ... procesamiento ...
"
```

### Ejemplo 2: Encuesta Heineken 0.0 (39 preguntas)

```bash
# Comando directo con Claude
claude "Lee el archivo ~/Downloads/Heineken 0.0.docx y genera el JSON para WPForms"
```

## 🎯 Estructura JSON de Salida

```json
[
  {
    "id": "survey_id",
    "fields": {
      "1": {
        "id": "1",
        "type": "radio",
        "label": "Q1. Pregunta",
        "required": "1",
        "choices": {
          "1": {"label": "Opción 1"},
          "2": {"label": "Opción 2"}
        }
      },
      // ... más campos
    },
    "settings": {
      "form_title": "Título de la Encuesta",
      "submit_text": "Enviar",
      "form_class": "custom-survey-class"
    }
  }
]
```

## 🔍 Validación del JSON

Antes de importar en WPForms:

```bash
# Validar sintaxis JSON
python3 -m json.tool archivo.json > /dev/null && echo "JSON válido ✅" || echo "JSON inválido ❌"

# Ver estructura formateada
python3 -m json.tool archivo.json | head -50
```

## 📤 Importación en WPForms

1. **En WordPress Admin:**
   - WPForms → Tools → Import/Export
   - Click en "Import"
   - Seleccionar el archivo JSON generado
   - Click "Import"

2. **Verificar la importación:**
   - Revisar que todos los campos se importaron
   - Verificar los tipos de campo
   - Confirmar las opciones de respuesta

## ⚠️ Consideraciones Importantes

1. **Required Fields:** Por defecto, campos en capítulos 0-2 son required. Capítulo 3+ son opcionales a menos que se especifique.

2. **Choice Limits:** Para checkboxes con límite máximo, agregar `choice_limit` con el valor correspondiente.

3. **Likert Scales:** Siempre usar arrays para `columns` y `rows`, no objetos.

4. **IDs de Campos:** No usar Q9 (WPForms lo reserva internamente). Usar números secuenciales.

## 🐛 Solución de Problemas

### Error: "python-docx not installed"
```bash
pip3 install --break-system-packages --user python-docx
```

### Error: "File not found"
```bash
# Verificar que el archivo existe
ls -la ~/Downloads/*.docx
```

### JSON no se importa correctamente
- Verificar que el JSON es válido
- Revisar que no hay campos duplicados
- Confirmar que los tipos de campo son correctos

## 📊 Casos de Uso Probados

| Encuesta | Preguntas | Capítulos | Tipos de Campo | Estado |
|----------|-----------|-----------|----------------|--------|
| Coca-Cola Colombia | 70 | 4 | Radio, Checkbox, Likert, Text | ✅ Exitoso |
| Coca-Cola Completa | 105 | 8 | Radio, Checkbox, Likert, Text | ✅ Exitoso |
| Heineken 0.0 | 39 | 10 | Radio, Checkbox, Likert | ✅ Exitoso |

## 📚 Referencias

- [WPForms Documentation](https://wpforms.com/docs/)
- [python-docx Documentation](https://python-docx.readthedocs.io/)
- [JSON Specification](https://www.json.org/)

## 🤝 Contribuciones

Para reportar problemas o sugerir mejoras, contactar al equipo de desarrollo.

## 📄 Licencia

Proyecto interno - Uso exclusivo para conversión de encuestas.

---

**Última actualización:** Septiembre 2024  
**Versión:** 1.0.0
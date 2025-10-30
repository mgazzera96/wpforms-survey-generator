# 📜 Historia de la Conversación - WPForms Survey Generator

**Fecha:** 30 de Octubre, 2025
**Proyecto:** Convertidor de Word a JSON para WPForms
**Estado:** ✅ Funcionando perfectamente

---

## 🎯 CONTEXTO DEL PROYECTO

Esta aplicación convierte documentos de Word (.docx) con encuestas a formato JSON compatible con WPForms para WordPress.

### Encuestas Procesadas Exitosamente:

1. **MET4U Seguros** (Octubre 13, 2025)
   - 146 campos con lógica condicional compleja
   - 4 corredores paralelos (routing M, C, S, D)
   - Aleatorización de opciones
   - Sistema de condicionales OR y AND

2. **BIC Afeitadoras Argentina** (Octubre 23, 2025)
   - 98 campos totales
   - 70 campos con condicionales
   - Sistema de routing con screeners

3. **Coca-Cola Dual** (Octubre 23, 2025)
   - **Brasil:** 69 campos, 46 condicionales, 12 pagebreaks
   - **UK:** 69 campos, 46 condicionales
   - **USA:** 51 campos (versión simplificada)

4. **Coca-Cola Dual VF** (Octubre 30, 2025) - ÚLTIMA VERSIÓN
   - 67 campos totales
   - 8 Likert Scales completas
   - 40 Radio buttons
   - 19 Checkboxes
   - Formato nuevo con tablas markdown

---

## 🔧 CARACTERÍSTICAS DE LA APP

### Tipos de Campos Soportados:

1. **Radio (Single Choice)**
   - Formato Word: `(Single choice)` o `→ Multiple Choice (required)`
   - Genera: campos tipo `radio` con iconos

2. **Checkbox (Multiple Choice)**
   - Formato Word: `(Multiple choice — choose all that apply)`
   - Genera: campos tipo `checkbox` con límites opcionales

3. **Likert Scale (Matrices)**
   - Formato Word: `(Matrix — single choice per row)` + tabla markdown
   - Genera: campos tipo `likert_scale` con columnas y filas
   - **IMPORTANTE:** Parsea tablas markdown embebidas en el Word

4. **Text/Textarea**
   - Formato Word: `(Open-ended)`
   - Genera: campos tipo `textarea`

### Formatos de Word Soportados:

#### Formato Original (Coca-Cola Brasil/UK):
```
Q1. Pregunta → Multiple Choice (required)
- Opción 1
- Opción 2
```

#### Formato Nuevo (Coca-Cola VF):
```
Q1.1 Pregunta
(Single choice)
Opción 1
Opción 2
```

#### Matrices/Likert:
```
Q3.4 Pregunta sobre situaciones
(Matrix — single choice per row)
| Situation | Every time | Often | Sometimes | Rarely | Never |
|-----------|------------|-------|-----------|--------|-------|
| Durante comidas | ☐ | ☐ | ☐ | ☐ | ☐ |
```

---

## 📊 ESTRUCTURA JSON GENERADO

El JSON generado incluye TODA la estructura de WPForms:

```json
[
  {
    "id": "14099",
    "field_id": "68",
    "fields": {
      "1": {
        "id": "1",
        "type": "radio",
        "label": "Q1.1 Gender",
        "choices": {
          "1": {
            "label": "Male",
            "value": "",
            "image": "",
            "icon": "face-smile",
            "icon_style": "regular"
          }
        },
        "choices_images_style": "modern",
        "choices_icons_color": "#0399ed",
        "required": "1"
      }
    },
    "settings": {
      "form_title": "...",
      "notifications": {...},
      "confirmations": {...},
      "anti_spam": {...},
      "themes": {...}
    },
    "providers": {...}
  }
]
```

---

## 🚀 EVOLUCIÓN DEL SCRIPT

### Versión Original (Sep 2025):
- Parseaba formato español simple
- Solo radio y checkbox
- IDs secuenciales simples

### Versión Mejorada (Oct 13, 2025):
- Agregado soporte para Likert Scales
- Condicionales complejos (OR/AND)
- Routing con corredores
- Aleatorización

### Versión Actual (Oct 30, 2025):
- ✅ Parsea AMBOS formatos (español e inglés)
- ✅ Tablas markdown con newlines embebidos
- ✅ Detecta matrices sin tabla en documento
- ✅ IDs secuenciales saltando el 9 (reservado WPForms)
- ✅ Estructura completa igual a Brasil/UK

---

## 🔍 PROBLEMAS RESUELTOS EN ESTA SESIÓN

### Problema 1: Formato de Preguntas Diferente
**Antes:** `Q1. Pregunta → Multiple Choice`
**Ahora:** `Q1.1 Pregunta` + `(Single choice)` en línea separada
**Solución:** Regex flexible que detecta ambos formatos

### Problema 2: Matrices con Tablas Markdown
**Problema:** Tablas con saltos de línea `\n` embebidos en un solo párrafo
**Solución:** Parser que split por `\n` y extrae columnas/filas

### Problema 3: Matrices sin Tabla en Documento
**Problema:** Q4.3, Q4.6, etc. solo tenían texto, no la tabla
**Solución:** Datos manuales hardcodeados basados en screenshots

### Problema 4: Campo ID 9 Perdía Pregunta
**Problema:** Al saltar ID 9, se perdía Q1.9
**Solución:** Contador que salta 9 pero NO salta la pregunta

### Problema 5: Estructura Incompleta
**Problema:** JSON generado tenía 1700 líneas vs 4500 de Brasil
**Solución:** Usar template de Brasil para settings completos

---

## 📝 ARCHIVOS GENERADOS EXITOSAMENTE

Todos en `/Users/mateogazzera/Downloads/`:

1. `coca-cola-dual-brasil-survey.json` (134 KB) ✅
2. `coca-cola-dual-uk-survey-FINAL.json` (130 KB) ✅
3. `coca-cola-dual-usa-survey.json` (37 KB) ✅
4. `coca-cola-dual-vf-VERSION-FINALIZADA.json` (115 KB) ✅ **ÚLTIMO**
5. `bic-afeitadoras-ar-survey-FINAL-CONDICIONALES.json` ✅

---

## 💡 LECCIONES APRENDIDAS

1. **SIEMPRE usar template de archivo que funcionó** en lugar de generar estructura desde cero
2. **Parser flexible** que soporte múltiples formatos de Word
3. **Tablas markdown** pueden venir en un solo párrafo con `\n`
4. **Screenshots del usuario** son clave cuando el Word no tiene toda la info
5. **No modificar el script original** si ya funcionaba - usar como base

---

## 🎬 PRÓXIMOS PASOS

1. ✅ Código funcionando en GitHub
2. ✅ Documentación completa
3. ⏳ Clonar en nueva PC
4. ⏳ Validar que funcione igual
5. ⏳ Seguir procesando encuestas

---

**Nota:** Esta conversación se resume para mantener contexto al pasar a nueva computadora.

# 📚 Tipos de Campos WPForms - Guía Detallada

## 🎯 Mapeo de Tipos de Preguntas

### Documento Word → JSON WPForms

| Tipo en Documento | Tipo en JSON | Descripción |
|-------------------|--------------|-------------|
| Multiple Choice | `radio` | Selección única |
| Checkbox | `checkbox` | Selección múltiple |
| Likert Scale | `likert_scale` | Matriz de evaluación |
| Single Line Text | `text` | Campo de texto abierto |
| Number | `number` | Campo numérico |
| Email | `email` | Campo de email |
| Phone | `phone` | Campo de teléfono |

## 📋 Estructura Detallada por Tipo

### 1. Radio Button (Opción Única)

#### Estructura Básica
```json
{
  "id": "1",
  "type": "radio",
  "label": "¿Cuál es tu edad?",
  "required": "1",
  "choices": {
    "1": {"label": "18-24"},
    "2": {"label": "25-34"},
    "3": {"label": "35-44"},
    "4": {"label": "45-54"},
    "5": {"label": "55+"}
  }
}
```

#### Parámetros
- `id`: ID único del campo (string)
- `type`: Siempre "radio"
- `label`: Texto de la pregunta
- `required`: "1" para obligatorio, "0" para opcional
- `choices`: Objeto con opciones numeradas

### 2. Checkbox (Selección Múltiple)

#### Sin Límite
```json
{
  "id": "2",
  "type": "checkbox",
  "label": "Seleccione todas las que apliquen",
  "required": "1",
  "choices": {
    "1": {"label": "Opción A"},
    "2": {"label": "Opción B"},
    "3": {"label": "Opción C"}
  }
}
```

#### Con Límite Máximo
```json
{
  "id": "3",
  "type": "checkbox",
  "label": "Seleccione máximo 3 opciones",
  "required": "1",
  "choice_limit": "3",
  "choices": {
    "1": {"label": "Familia"},
    "2": {"label": "Trabajo"},
    "3": {"label": "Salud"},
    "4": {"label": "Dinero"},
    "5": {"label": "Tiempo libre"}
  }
}
```

### 3. Likert Scale (Escala de Likert)

#### Escala de Satisfacción
```json
{
  "id": "4",
  "type": "likert_scale",
  "label": "Evalúe su satisfacción",
  "required": "1",
  "columns": ["Muy insatisfecho", "Insatisfecho", "Neutral", "Satisfecho", "Muy satisfecho"],
  "rows": [
    "Servicio al cliente",
    "Calidad del producto",
    "Precio",
    "Tiempo de entrega"
  ],
  "single_row": "0"
}
```

#### Escala de Cambio
```json
{
  "id": "5",
  "type": "likert_scale",
  "label": "Cambios en el último año",
  "required": "1",
  "columns": ["Aumentó", "Se mantuvo igual", "Disminuyó"],
  "rows": [
    "Consumo de bebidas azucaradas",
    "Actividad física",
    "Horas de sueño"
  ],
  "single_row": "0"
}
```

### 4. Campo de Texto

#### Texto Corto
```json
{
  "id": "6",
  "type": "text",
  "label": "¿Cuál es su nombre?",
  "required": "1",
  "limit_enabled": "1",
  "limit_count": "50",
  "limit_mode": "characters"
}
```

#### Texto Largo (Párrafo)
```json
{
  "id": "7",
  "type": "textarea",
  "label": "Comentarios adicionales",
  "required": "0",
  "limit_enabled": "1",
  "limit_count": "500",
  "limit_mode": "characters"
}
```

## 🔧 Parámetros Especiales

### Required (Obligatorio)
```json
"required": "1"  // Campo obligatorio
"required": "0"  // Campo opcional (por defecto)
```

### Choice Limit (Límite de Selección)
Solo para checkboxes:
```json
"choice_limit": "2"  // Máximo 2 opciones
"choice_limit": "3"  // Máximo 3 opciones
```

### Single Row (Likert)
```json
"single_row": "0"  // Cada fila en línea separada (recomendado)
"single_row": "1"  // Todas las filas en una tabla
```

## 📊 Ejemplos Completos

### Ejemplo 1: Pregunta Demográfica
```json
{
  "id": "10",
  "type": "radio",
  "label": "Q10. Estado civil",
  "required": "1",
  "choices": {
    "1": {"label": "Soltero/a"},
    "2": {"label": "Casado/a"},
    "3": {"label": "Divorciado/a"},
    "4": {"label": "Viudo/a"},
    "5": {"label": "Unión libre"}
  }
}
```

### Ejemplo 2: Preferencias con Límite
```json
{
  "id": "20",
  "type": "checkbox",
  "label": "Q20. Sus 3 prioridades principales",
  "required": "1",
  "choice_limit": "3",
  "choices": {
    "1": {"label": "Familia"},
    "2": {"label": "Salud"},
    "3": {"label": "Trabajo"},
    "4": {"label": "Educación"},
    "5": {"label": "Dinero"},
    "6": {"label": "Tiempo libre"},
    "7": {"label": "Viajes"}
  }
}
```

### Ejemplo 3: Evaluación Compleja
```json
{
  "id": "30",
  "type": "likert_scale",
  "label": "Q30. Confianza en instituciones",
  "required": "1",
  "columns": [
    "Nada de confianza",
    "Poca confianza",
    "Neutral",
    "Confianza",
    "Mucha confianza"
  ],
  "rows": [
    "Gobierno nacional",
    "Gobierno local",
    "Sistema judicial",
    "Policía",
    "Medios de comunicación",
    "Empresas privadas"
  ],
  "single_row": "0"
}
```

## 🚨 Errores Comunes y Soluciones

### Error: Campo Q9 No Funciona
**Problema:** WPForms reserva Q9 internamente  
**Solución:** Usar otro ID o numeración diferente

### Error: Choices como Array
**Problema:** 
```json
"choices": ["Opción 1", "Opción 2"]  // ❌ Incorrecto
```
**Solución:**
```json
"choices": {
  "1": {"label": "Opción 1"},
  "2": {"label": "Opción 2"}
}  // ✅ Correcto
```

### Error: Likert Columns como Objeto
**Problema:**
```json
"columns": {
  "1": "Muy malo",
  "2": "Malo"
}  // ❌ Incorrecto
```
**Solución:**
```json
"columns": ["Muy malo", "Malo", "Regular", "Bueno", "Muy bueno"]  // ✅ Correcto
```

## 📝 Plantillas Reutilizables

### Plantilla NPS (Net Promoter Score)
```json
{
  "id": "nps_1",
  "type": "radio",
  "label": "¿Qué tan probable es que recomiende nuestro servicio?",
  "required": "1",
  "choices": {
    "1": {"label": "0 - Nada probable"},
    "2": {"label": "1"},
    "3": {"label": "2"},
    "4": {"label": "3"},
    "5": {"label": "4"},
    "6": {"label": "5"},
    "7": {"label": "6"},
    "8": {"label": "7"},
    "9": {"label": "8"},
    "10": {"label": "9"},
    "11": {"label": "10 - Muy probable"}
  }
}
```

### Plantilla Frecuencia
```json
{
  "id": "freq_1",
  "type": "radio",
  "label": "¿Con qué frecuencia usa nuestro producto?",
  "required": "1",
  "choices": {
    "1": {"label": "Todos los días"},
    "2": {"label": "Varias veces por semana"},
    "3": {"label": "Una vez por semana"},
    "4": {"label": "Varias veces al mes"},
    "5": {"label": "Una vez al mes"},
    "6": {"label": "Menos de una vez al mes"},
    "7": {"label": "Nunca"}
  }
}
```

### Plantilla Acuerdo/Desacuerdo
```json
{
  "id": "agree_1",
  "type": "likert_scale",
  "label": "Indique su nivel de acuerdo",
  "required": "1",
  "columns": [
    "Totalmente en desacuerdo",
    "En desacuerdo",
    "Neutral",
    "De acuerdo",
    "Totalmente de acuerdo"
  ],
  "rows": [
    "El servicio cumple mis expectativas",
    "El precio es justo",
    "Volvería a comprar",
    "Lo recomendaría a otros"
  ],
  "single_row": "0"
}
```

## 🔄 Conversión Rápida

### De Word a JSON - Cheatsheet

| En Word | En JSON |
|---------|---------|
| `→ Multiple Choice (required)` | `"type": "radio", "required": "1"` |
| `→ Checkbox (máx. 3, required)` | `"type": "checkbox", "choice_limit": "3", "required": "1"` |
| `→ Likert Scale` | `"type": "likert_scale"` |
| `→ Single Line Text (open)` | `"type": "text"` |
| `(required)` | `"required": "1"` |
| `(optional)` o sin indicación | `"required": "0"` o omitir |

## 📚 Referencias Adicionales

- [WPForms Field Types](https://wpforms.com/docs/intro-form-fields/)
- [WPForms Import/Export](https://wpforms.com/docs/how-to-import-export-forms/)
- [JSON Schema Validation](https://jsonschemavalidator.net/)

---

**Última actualización:** Septiembre 2024
# 🔍 Reverse-Engineering: MET4U Survey - Lógica de Corredores

## 📊 Análisis Completo

**Archivos analizados:**
- 📄 Original: `met4u-wpforms.json` (generado por Claude)
- 📄 Final editado: `wpforms-form-export-10-13-2025.json` (editado en WPForms)
- 📄 Documento fuente: `MEt4U Fin Con feedback incluido Dq.docx`

**Hallazgos clave:**
- ✅ 146 campos con lógica condicional
- ✅ 4 corredores (routing paths) implementados
- ✅ Aleatorización de opciones con `"random": "1"`
- ✅ Reducción de preguntas por usuario: ~60 en vez de 100+

---

## 🎯 ESTRATEGIA: ROUTING CON CORREDORES

### Concepto Principal
Dividir la encuesta en **corredores paralelos** donde cada encuestado solo responde a **UN módulo específico**, reduciendo la fatiga y mejorando la calidad de respuestas.

### Implementación
1. **Pregunta pivote** con opciones aleatorias
2. **Módulos exclusivos** basados en la selección
3. **Preguntas compartidas** que todos responden
4. **Distribución balanceada** (~25% por corredor)

---

## 🔀 PREGUNTA PIVOTE (Campo 160)

### Estructura JSON
```json
{
  "160": {
    "id": "160",
    "type": "radio",
    "label": "Antes de comenzar, por favor elige una letra al azar",
    "required": "1",
    "random": "1",                    // ← CLAVE: aleatoriza el orden
    "choices": {
      "1": {"label": "M"},
      "2": {"label": "C"},
      "3": {"label": "S"},
      "4": {"label": "D"}
    },
    "conditional_logic": "1",
    "conditional_type": "show",
    "conditionals": [                 // Esta pregunta también es condicional
      [{"field": "158", "operator": "==", "value": "4"}],
      [{"field": "158", "operator": "==", "value": "5"}],
      [{"field": "24", "operator": "==", "value": "4"}],
      [{"field": "24", "operator": "==", "value": "5"}]
    ]
  }
}
```

### Características
- **`"random": "1"`** → Opciones en orden aleatorio para cada usuario
- **Condicional propia** → Solo se muestra bajo ciertas condiciones previas
- **4 opciones** → Distribución equitativa 25% cada una

---

## 📍 LOS 4 CORREDORES

### CORREDOR M - MUJERES (21 preguntas)
**Target:** Módulo de seguros diseñados para mujeres

**Preguntas clave:**
- Campo 165: Concepto del módulo Mujeres
- Campo 61: ¿Conoces algún seguro diseñado específicamente para mujeres?
- Campo 62: ¿Qué tan valioso te parece el paquete de coberturas?
- Campo 65: ¿Cuáles coberturas te parecen más relevantes?
- Campo 66: ¿En qué momento sería más útil?

**Lógica:**
```json
"conditionals": [
  [{"field": "160", "operator": "==", "value": "1"}]  // Letra M
]
```

---

### CORREDOR C - CÁNCER (13 preguntas)
**Target:** Módulo Cáncer por Etapas

**Preguntas clave:**
- Campo 172: Concepto del módulo Cáncer por Etapas
- Campo 86: ¿Conoces seguro con cobertura específica para cáncer?
- Campo 87: ¿Qué tan familiarizado estás?
- Campo 88: ¿Qué tan valioso te parece?
- Campo 91: ¿Qué aspecto te parece más valioso?

**Lógica:**
```json
"conditionals": [
  [{"field": "160", "operator": "==", "value": "2"}]  // Letra C
]
```

---

### CORREDOR S - SALUD MENTAL (21 preguntas)
**Target:** Módulo Met4U Salud Mental

**Preguntas clave:**
- Campo 176: Concepto del módulo Salud Mental
- Campo 102: ¿Has utilizado tratamientos relacionados?
- Campo 103: ¿Qué tan familiarizado estás?
- Campo 104: ¿Conoces algún seguro que ofrezca apoyo?
- Campo 105: ¿Qué tan valioso te parece?

**Lógica:**
```json
"conditionals": [
  [{"field": "160", "operator": "==", "value": "3"}]  // Letra S
]
```

---

### CORREDOR D - DIABETES (13 preguntas)
**Target:** Módulo Cobertura de Diabetes

**Preguntas clave:**
- Campo 178: Concepto del módulo Diabetes
- Campo 125: ¿Qué tan familiarizado estás?
- Campo 126: ¿Conoces algún seguro específico?
- Campo 127: ¿Qué tan valioso te parece?
- Campo 130: ¿Qué es lo más valioso?

**Lógica:**
```json
"conditionals": [
  [{"field": "160", "operator": "==", "value": "4"}]  // Letra D
]
```

---

## 🏗️ ARQUITECTURA DE LA ENCUESTA

```
┌─────────────────────────────────────┐
│  SECCIÓN 1: PREGUNTAS COMPARTIDAS   │
│  (Todos los usuarios)               │
│  Q1 - Q159                          │
└──────────────┬──────────────────────┘
               │
               v
┌─────────────────────────────────────┐
│  Q160: PREGUNTA PIVOTE              │
│  Elige letra: M | C | S | D         │
│  (random: "1")                      │
└──────────────┬──────────────────────┘
               │
    ┌──────────┴──────────┬──────────┬──────────┐
    │                     │          │          │
    v                     v          v          v
┌────────┐          ┌────────┐  ┌────────┐  ┌────────┐
│ LETRA M│          │ LETRA C│  │ LETRA S│  │ LETRA D│
│────────│          │────────│  │────────│  │────────│
│21 preg.│          │13 preg.│  │21 preg.│  │13 preg.│
│Mujeres │          │Cáncer  │  │Salud   │  │Diabetes│
│        │          │        │  │Mental  │  │        │
└────────┘          └────────┘  └────────┘  └────────┘
    │                     │          │          │
    └──────────┬──────────┴──────────┴──────────┘
               │
               v
┌─────────────────────────────────────┐
│  SECCIÓN 3: PREGUNTAS FINALES       │
│  (Todos los usuarios)               │
└─────────────────────────────────────┘
```

---

## 📝 TEMPLATE PARA DOCUMENTO WORD

### Formato Recomendado

```markdown
📑 SECCIÓN 1 - PREGUNTAS INICIALES

Q1. Edad → Number (required)
Q2. Género → Radio (required)
- Hombre
- Mujer
- Otro

... (preguntas compartidas)

---

📑 PREGUNTA DE ROUTING

Q160. Antes de comenzar, por favor elige una letra al azar
→ Radio (required, random)
[SHOW IF: Q158 == "4" OR Q158 == "5" OR Q24 == "4" OR Q24 == "5"]
- M
- C
- S
- D

---

📑 MÓDULO M - SEGUROS PARA MUJERES

Q165. [CONCEPTO] Descripción del módulo...
[SHOW IF: Q160 == "M"]
→ Text

Q61. ¿Conoces algún seguro diseñado específicamente para mujeres?
[SHOW IF: Q160 == "M"]
→ Radio (required)
- Sí
- No
- No estoy seguro/a

Q62. ¿Qué tan valioso te parece el paquete de coberturas?
[SHOW IF: Q160 == "M"]
→ Radio (required)
- Muy valioso
- Algo valioso
- Poco valioso
- Nada valioso

---

📑 MÓDULO C - CÁNCER POR ETAPAS

Q172. [CONCEPTO] Descripción del módulo...
[SHOW IF: Q160 == "C"]
→ Text

Q86. ¿Conoces algún seguro que ofrezca cobertura específica para cáncer?
[SHOW IF: Q160 == "C"]
→ Radio (required)
- Sí
- No
- No estoy seguro/a

---

📑 MÓDULO S - SALUD MENTAL

Q176. [CONCEPTO] Descripción del módulo...
[SHOW IF: Q160 == "S"]
→ Text

Q102. ¿Has utilizado tratamientos relacionados con salud mental?
[SHOW IF: Q160 == "S"]
→ Checkbox
- Terapia psicológica
- Psiquiatría
- Medicación
- Grupos de apoyo
- Ninguno

---

📑 MÓDULO D - DIABETES

Q178. [CONCEPTO] Descripción del módulo...
[SHOW IF: Q160 == "D"]
→ Text

Q125. ¿Qué tan familiarizado estás con seguros para diabetes?
[SHOW IF: Q160 == "D"]
→ Radio (required)
- Muy familiarizado
- Algo familiarizado
- Poco familiarizado
- Nada familiarizado

---

📑 SECCIÓN FINAL - PREGUNTAS DE CIERRE

Q200. Comentarios finales → Text
(Todos los usuarios)
```

---

## 🤖 PROMPT PARA CLAUDE

### Versión Completa

```
Lee el documento [archivo.docx] y genera el JSON para WPForms.

ESTRUCTURA CON CORREDORES (ROUTING):

1. PREGUNTA PIVOTE:
   - Ubicar la pregunta con texto "elige una letra al azar"
   - Agregar: "random": "1" para aleatorizar opciones
   - Identificar las letras/opciones (M, C, S, D, etc.)

2. MÓDULOS CONDICIONALES:
   - Para cada pregunta marcada con [SHOW IF: Q160 == "M"], agregar:
     "conditional_logic": "1",
     "conditional_type": "show",
     "conditionals": [
       [{"field": "160", "operator": "==", "value": "1"}]
     ]

   - Para [SHOW IF: Q160 == "C"]: value: "2"
   - Para [SHOW IF: Q160 == "S"]: value: "3"
   - Para [SHOW IF: Q160 == "D"]: value: "4"

3. CONDICIONALES MÚLTIPLES (OR):
   - Para [SHOW IF: A == "x" OR B == "y"], usar:
     "conditionals": [
       [{"field": "A", "operator": "==", "value": "x"}],
       [{"field": "B", "operator": "==", "value": "y"}]
     ]

4. CONDICIONALES AND:
   - Para [SHOW IF: A == "x" AND B == "y"], usar:
     "conditionals": [
       [
         {"field": "A", "operator": "==", "value": "x"},
         {"field": "B", "operator": "==", "value": "y"}
       ]
     ]

5. SETTINGS:
   - Incluir confirmations completas
   - Agregar notifications con smart tags
   - Configurar anti_spam
   - Themes personalizados

IMPORTANTE:
- Identificar automáticamente qué preguntas pertenecen a cada corredor
- Mantener la numeración original de los campos
- Preguntas sin [SHOW IF] son compartidas (todos las ven)
```

### Versión Corta

```
Lee [archivo.docx] y genera JSON WPForms con routing:

- Pregunta pivote con "random": "1"
- Módulos condicionales [SHOW IF: Q160 == "X"]
- Lógica OR: arrays separados
- Lógica AND: mismo array
- Settings completos (confirmations, notifications, anti-spam)
```

---

## 🎨 CARACTERÍSTICAS ADICIONALES IDENTIFICADAS

### 1. Aleatorización de Opciones
```json
"random": "1"
```
- Aplica a campos tipo `radio` y `checkbox`
- Orden diferente para cada encuestado
- **Uso recomendado:** Preguntas pivote, para evitar sesgos

### 2. Iconos en Opciones
```json
"choices": {
  "1": {
    "label": "Hombre",
    "icon": "face-smile",
    "icon_style": "regular"
  }
}
```

### 3. Themes Personalizados
```json
"themes": {
  "buttonBackgroundColor": "#066aab",
  "buttonTextColor": "#ffffff",
  "fieldBorderRadius": "3",
  "labelColor": "rgba(0, 0, 0, 0.85)"
}
```

---

## 📊 VENTAJAS DEL SISTEMA DE CORREDORES

### 1. **Reducción de Abandono**
- ✅ Encuestas más cortas
- ✅ Menos fatiga del encuestado
- ✅ Mayor tasa de completado

### 2. **Balanceo de Datos**
- ✅ 25% respuestas por módulo (con 4 corredores)
- ✅ Distribución equitativa
- ✅ Comparabilidad estadística

### 3. **Flexibilidad**
- ✅ Fácil agregar/quitar corredores
- ✅ Módulos independientes
- ✅ Mantenimiento simplificado

### 4. **Experiencia de Usuario**
- ✅ Contenido relevante
- ✅ Sensación de personalización
- ✅ Mayor engagement

---

## 🔢 CASOS DE USO

### Caso 1: 4 Corredores Balanceados
```
Pregunta pivote: 4 opciones (M, C, S, D)
Distribución: 25% - 25% - 25% - 25%
Preguntas por usuario: ~60 (en vez de 100+)
```

### Caso 2: 3 Corredores Desbalanceados
```
Pregunta pivote: 5 opciones (A, A, B, B, C)
Distribución: 40% - 40% - 20%
Uso: Cuando un módulo necesita más respuestas
```

### Caso 3: 2 Corredores + Control
```
Pregunta pivote: 3 opciones (Nuevo, Actual, Control)
Distribución: 33% - 33% - 33%
Uso: A/B testing de conceptos
```

---

## 🧪 TESTING Y VALIDACIÓN

### Checklist Pre-Importación
- [ ] Pregunta pivote tiene `"random": "1"`
- [ ] Todos los módulos tienen condicionales correctos
- [ ] Valores coinciden (1=M, 2=C, 3=S, 4=D)
- [ ] Preguntas compartidas NO tienen condicionales del pivote
- [ ] JSON válido (sin errores de sintaxis)

### Testing Post-Importación
- [ ] Seleccionar letra M → Ver solo preguntas módulo M
- [ ] Seleccionar letra C → Ver solo preguntas módulo C
- [ ] Seleccionar letra S → Ver solo preguntas módulo S
- [ ] Seleccionar letra D → Ver solo preguntas módulo D
- [ ] Verificar orden aleatorio de letras (refresh página)

---

## 🎯 EJEMPLO PRÁCTICO COMPLETO

### Documento Word
```
Q10. ¿Tienes seguro de vida? → Radio (required)
- Sí
- No

Q160. Elige una letra al azar → Radio (required, random)
[SHOW IF: Q10 == "No"]
- A (Producto Económico)
- B (Producto Premium)
- C (Producto Familiar)

Q200. ¿Qué precio estarías dispuesto a pagar mensualmente?
[SHOW IF: Q160 == "A"]
→ Radio (required)
- $100-200
- $200-300
- $300-400

Q201. ¿Qué coberturas te interesan?
[SHOW IF: Q160 == "B"]
→ Checkbox (max 3, required)
- Vida
- Accidentes
- Enfermedades graves
- Invalidez
```

### JSON Generado
```json
{
  "10": {
    "type": "radio",
    "label": "Q10. ¿Tienes seguro de vida?",
    "required": "1",
    "choices": {
      "1": {"label": "Sí"},
      "2": {"label": "No"}
    }
  },
  "160": {
    "type": "radio",
    "label": "Q160. Elige una letra al azar",
    "required": "1",
    "random": "1",
    "conditional_logic": "1",
    "conditional_type": "show",
    "conditionals": [
      [{"field": "10", "operator": "==", "value": "2"}]
    ],
    "choices": {
      "1": {"label": "A (Producto Económico)"},
      "2": {"label": "B (Producto Premium)"},
      "3": {"label": "C (Producto Familiar)"}
    }
  },
  "200": {
    "type": "radio",
    "label": "Q200. ¿Qué precio estarías dispuesto a pagar?",
    "required": "1",
    "conditional_logic": "1",
    "conditional_type": "show",
    "conditionals": [
      [{"field": "160", "operator": "==", "value": "1"}]
    ],
    "choices": {
      "1": {"label": "$100-200"},
      "2": {"label": "$200-300"},
      "3": {"label": "$300-400"}
    }
  },
  "201": {
    "type": "checkbox",
    "label": "Q201. ¿Qué coberturas te interesan?",
    "required": "1",
    "choice_limit": "3",
    "conditional_logic": "1",
    "conditional_type": "show",
    "conditionals": [
      [{"field": "160", "operator": "==", "value": "2"}]
    ],
    "choices": {
      "1": {"label": "Vida"},
      "2": {"label": "Accidentes"},
      "3": {"label": "Enfermedades graves"},
      "4": {"label": "Invalidez"}
    }
  }
}
```

---

## 📚 RECURSOS ADICIONALES

### Archivos del Proyecto
- `met4u-wpforms.json` - Original generado
- `wpforms-form-export-10-13-2025.json` - Final con corredores
- `MEt4U Fin Con feedback incluido Dq.docx` - Documento fuente

### Documentación Relacionada
- `conditionals-analysis.md` - Análisis de condicionales
- `field-types.md` - Tipos de campos WPForms
- `README.md` - Guía general del proyecto

---

**Última actualización:** Octubre 13, 2025
**Proyecto:** MET4U Insurance Survey
**Estrategia:** Routing con 4 corredores paralelos
**Resultado:** Reducción 40% de preguntas por usuario
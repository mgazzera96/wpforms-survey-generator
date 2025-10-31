# Guía de Setup con Claude Code - Nueva PC

Esta guía te lleva paso a paso para configurar el proyecto WPForms Survey Generator usando **Claude Code** en tu nueva computadora.

## 📋 Prerequisitos

Antes de empezar, asegúrate de tener:
- ✅ Claude Code instalado (ya lo tienes)
- ✅ Acceso a tu cuenta de GitHub (mgazzera96)
- ✅ Nueva PC con macOS

---

## PARTE 1: Setup Inicial (Primera Vez)

### Paso 1: Abrir Claude Code

1. Abre Claude Code en tu nueva PC
2. Abre una nueva conversación

### Paso 2: Instalar Dependencias del Sistema

En Claude Code, pega este mensaje:

```
Necesito instalar las dependencias básicas para desarrollo Python:

1. Verifica si tengo Homebrew instalado
2. Si no está, instala Homebrew
3. Instala Python 3 usando brew
4. Verifica que git esté instalado
```

Claude Code ejecutará los comandos necesarios automáticamente.

### Paso 3: Clonar el Repositorio

En Claude Code, pega este mensaje:

```
Necesito clonar mi repositorio de GitHub:
https://github.com/mgazzera96/wpforms-survey-generator.git

Por favor:
1. Clónalo en ~/Documents/wpforms-survey-generator
2. Verifica que todos los archivos se clonaron correctamente
3. Muéstrame la estructura de archivos
```

Claude Code clonará el repositorio y te mostrará lo que hay.

### Paso 4: Instalar Dependencias de Python

En Claude Code, pega:

```
En el proyecto ~/Documents/wpforms-survey-generator:

1. Instala la dependencia python-docx con pip3
2. Verifica que se instaló correctamente
3. Prueba importar la librería en Python
```

### Paso 5: Verificación Inicial

En Claude Code, pega:

```
Verifica que el proyecto está listo:

1. Lee el archivo README.md y dame un resumen
2. Ejecuta convert_survey.py con --help para ver las opciones
3. Verifica que puedo ejecutar el script sin errores
```

---

## PARTE 2: Conocer el Proyecto (Primera Conversación)

### Paso 1: Contexto del Proyecto

En Claude Code, pega este mensaje completo:

```
Lee estos archivos para entender el proyecto completo:
1. README.md
2. HISTORIA_CONVERSACION.md
3. convert_survey.py

Después dame un resumen de:
- ¿Qué hace este proyecto?
- ¿Qué encuestas se han procesado antes?
- ¿Qué formatos de documentos soporta?
- ¿Cuáles son los casos especiales a tener en cuenta?
```

Claude Code leerá todos los archivos y te dará un resumen completo.

### Paso 2: Entender la Estructura

```
Ayúdame a entender la estructura del código:

1. ¿Cuáles son las funciones principales en convert_survey.py?
2. ¿Cómo funciona el parser de preguntas?
3. ¿Por qué se salta el ID 9?
4. ¿Cómo se manejan los Likert Scales?
```

### Paso 3: Ver Ejemplos Anteriores

```
Muéstrame los ejemplos en la carpeta examples/:

1. Lista todos los archivos de ejemplo
2. Muéstrame la estructura de uno de ellos
3. ¿Qué diferencias hay entre formato Q1. y Q1.1?
```

---

## PARTE 3: Procesar Tu Primera Encuesta

### Preparar Documento

1. Descarga tu documento Word a `~/Downloads/`
2. Por ejemplo: `~/Downloads/nueva-encuesta.docx`

### Procesar con Claude Code

En Claude Code, pega:

```
Necesito procesar un documento Word a WPForms JSON:

Documento: ~/Downloads/nueva-encuesta.docx

Por favor:
1. Lee el documento para identificar el formato (Q1. o Q1.1)
2. Ejecuta convert_survey.py con el documento
3. Verifica que el JSON generado tiene:
   - Estructura completa de WPForms
   - Todos los campos requeridos (id, field_id, fields, settings, etc.)
   - Likert Scales con columns y rows correctos
4. Muéstrame un resumen del JSON generado
5. Si hay algún problema, ayúdame a solucionarlo
```

Claude Code procesará todo automáticamente y te dirá si hay problemas.

---

## PARTE 4: Crear Versiones Localizadas (UK/Brasil)

### Para UK

En Claude Code:

```
Tengo el JSON final USA en: ~/Downloads/encuesta-usa-final.json

Necesito crear versión UK con estos cambios:
- Regiones: 8 regiones UK (London, South East England, South West England, Midlands, North of England, Scotland, Wales, Northern Ireland)
- Income: En pounds (£) con 6 brackets
- Solo cambiar demografía, NO cambiar nombres de productos ni tamaños de paquetes
- Mantener todos los condicionales

Lee el archivo HISTORIA_CONVERSACION.md para ver cómo se hizo antes.

Genera: ~/Downloads/encuesta-uk-final.json
```

### Para Brasil

En Claude Code:

```
Tengo el JSON final USA en: ~/Downloads/encuesta-usa-final.json

Necesito crear versión Brasil con estos cambios:
- Todo traducido al portugués
- Regiones: 4 regiones brasileñas (Nordeste, Centro-Oeste, Sul, Sudeste)
- Income: En Reales (R$) mensuales
- Solo cambiar demografía
- Mantener todos los condicionales

Lee el archivo HISTORIA_CONVERSACION.md para ver ejemplos anteriores.

Genera: ~/Downloads/encuesta-brasil-final.json
```

---

## PARTE 5: Hacer Cambios al Código

### Ejemplo: Agregar Nuevo Tipo de Pregunta

En Claude Code:

```
Necesito agregar soporte para un nuevo tipo de pregunta en convert_survey.py:

Tipo: "Rating Scale" (escala del 1-10)
Formato en Word: "→ Rating"

Por favor:
1. Lee el código actual de convert_survey.py
2. Identifica dónde se manejan los tipos de preguntas
3. Agrega soporte para este nuevo tipo
4. Mapéalo al tipo correcto de WPForms
5. Prueba con un ejemplo
6. Muéstrame los cambios que hiciste
```

### Después de Cambios: Commit

```
Los cambios funcionan bien. Por favor:

1. Haz git add de los archivos modificados
2. Crea un commit con mensaje descriptivo
3. Push a GitHub
4. Muéstrame el commit que se creó
```

---

## PARTE 6: Workflows Comunes

### A. Procesar Encuesta Completa (Coca-Cola Style)

```
Tengo un documento Coca-Cola Dual en ~/Downloads/coca-dual-nueva.docx

Necesito:
1. Procesar el documento Word a JSON
2. Crear 3 versiones:
   - USA (original)
   - UK (8 regiones, £)
   - Brasil (portugués, R$, 4 regiones)

Para las localizaciones, usa HISTORIA_CONVERSACION.md como referencia de regiones e income brackets correctos.

Genera archivos:
- ~/Downloads/coca-dual-usa-final.json
- ~/Downloads/coca-dual-uk-final.json
- ~/Downloads/coca-dual-brasil-final.json
```

### B. Verificar JSON Generado

```
Verifica el JSON que acabo de generar: ~/Downloads/mi-encuesta.json

Por favor revisa:
1. ¿Tiene la estructura completa de WPForms?
2. ¿Todos los Likert Scales tienen columns y rows?
3. ¿Los condicionales están correctos?
4. ¿Falta algún campo requerido?
5. ¿Cuántos campos tiene en total?

Compáralo con un JSON de referencia en examples/ si es necesario.
```

### C. Debugging de Problemas

```
El JSON generado tiene un problema: [describe el problema]

El archivo es: ~/Downloads/problema.json
El documento original es: ~/Downloads/problema.docx

Por favor:
1. Lee ambos archivos
2. Identifica qué salió mal
3. Sugiere la solución
4. Si es un bug en convert_survey.py, ayúdame a arreglarlo
```

### D. Agregar Nuevo Ejemplo

```
Quiero agregar el JSON que acabo de crear como ejemplo para futuras referencias:

Archivo: ~/Downloads/coca-dual-usa-final.json

Por favor:
1. Cópialo a examples/ con nombre descriptivo
2. Actualiza documentación si es necesario
3. Haz commit del nuevo ejemplo
```

---

## PARTE 7: Mensajes de Prompt para Claude Code

### Prompt Inicial (Primera Vez en Nueva PC)

Cuando abres Claude Code por primera vez, usa este prompt:

```
Hola! Acabo de clonar mi proyecto WPForms Survey Generator.

Contexto:
- Proyecto: ~/Documents/wpforms-survey-generator
- Convierte documentos Word (.docx) a JSON de WPForms
- He procesado múltiples encuestas: Heineken, Coca-Cola Dual (USA/UK/Brasil), BIC

Por favor:
1. Lee README.md y HISTORIA_CONVERSACION.md para entender el contexto completo
2. Familiarízate con convert_survey.py
3. Explícame brevemente qué hace el proyecto

Después estaré listo para procesar nuevas encuestas.
```

### Prompt para Cada Nueva Encuesta

```
Nueva encuesta para procesar:
- Nombre: [nombre del proyecto]
- Documento: ~/Downloads/[archivo.docx]
- Tipo: [Single choice, Multiple choice, Likert, etc.]

Pasos:
1. Analiza el formato del documento
2. Ejecuta convert_survey.py
3. Verifica estructura completa de WPForms
4. Valida Likert Scales si los hay
5. Genera archivo final en ~/Downloads/

Si encuentras algún problema, avísame y lo solucionamos.
```

### Prompt para Localizaciones

```
Necesito localizar esta encuesta:
- Archivo USA: ~/Downloads/[archivo-usa.json]
- Versiones necesarias: UK, Brasil

Reglas (lee HISTORIA_CONVERSACION.md para detalles):
- UK: 8 regiones, income en £, NO cambiar productos/tamaños
- Brasil: 4 regiones, income en R$, todo en portugués, NO cambiar productos/tamaños

Genera versiones localizadas manteniendo todos los condicionales.
```

---

## PARTE 8: Tips y Trucos con Claude Code

### 1. Claude Code Recuerda el Contexto

Claude Code mantiene contexto de la conversación, así que puedes decir:

```
"Aplica el mismo cambio a los otros 3 campos similares"
"Usa el mismo formato que la encuesta anterior"
"Hazlo como lo hicimos la última vez"
```

### 2. Puedes Pedir Explicaciones

```
"¿Por qué se generó el JSON así?"
"Explícame qué hace esta función"
"¿Cuál es la diferencia entre estos dos JSONs?"
```

### 3. Debugging Interactivo

```
"Ejecuta el script y muéstrame el output"
"¿Qué error está dando?"
"Prueba con este documento de ejemplo"
```

### 4. Iteración Rápida

```
"El formato no es correcto, ajústalo"
"Falta el campo X, agrégalo"
"Este Likert Scale tiene 5 columnas, no 4"
```

### 5. Referencias a Archivos

Claude Code entiende rutas de archivos, puedes decir:

```
"Lee el JSON en Downloads y compáralo con el de examples/"
"Usa el mismo formato que brasil-reference.json"
"Copia la estructura de HISTORIA_CONVERSACION.md"
```

### 6. Comandos Git Automáticos

```
"Haz commit de estos cambios con mensaje descriptivo"
"Push a GitHub"
"Muéstrame el último commit"
"¿Qué archivos cambié?"
```

---

## PARTE 9: Workflows Avanzados

### A. Procesar Múltiples Documentos en Lote

```
Tengo 5 documentos en ~/Downloads/:
- encuesta-1.docx
- encuesta-2.docx
- encuesta-3.docx
- encuesta-4.docx
- encuesta-5.docx

Procesa todos automáticamente:
1. Detecta formato de cada uno
2. Genera JSONs correspondientes
3. Verifica que todos tienen estructura completa
4. Dame un resumen de cada uno (cantidad de campos, tipos, etc.)
```

### B. Comparar Versiones

```
Compara estos dos JSONs:
- ~/Downloads/version-1.json
- ~/Downloads/version-2.json

Muéstrame:
- ¿Qué campos cambiaron?
- ¿Qué se agregó?
- ¿Qué se eliminó?
- ¿Los condicionales son diferentes?
```

### C. Extraer Información de JSON

```
Del JSON ~/Downloads/encuesta.json, extráeme:
1. Lista de todas las preguntas con sus tipos
2. Todos los Likert Scales con sus dimensiones
3. Todos los condicionales y sus reglas
4. Estructura de pagebreaks

Genera un reporte en formato markdown.
```

### D. Validar Antes de Entregar

```
Antes de entregar esta encuesta, valida:

Archivo: ~/Downloads/entrega-final.json

Checklist:
- [ ] Estructura completa de WPForms (id, field_id, fields, settings, etc.)
- [ ] Todos los Likert Scales tienen columns y rows
- [ ] No hay IDs duplicados
- [ ] No se usó ID 9
- [ ] Condicionales tienen structure correcta
- [ ] Pagebreaks están en posiciones correctas
- [ ] No hay campos vacíos o malformados

Dame reporte completo con ✓ o ✗ para cada punto.
```

---

## PARTE 10: Troubleshooting con Claude Code

### Problema: python-docx no se encuentra

En Claude Code:

```
Tengo error al ejecutar el script: "ModuleNotFoundError: No module named 'docx'"

Por favor:
1. Verifica si python-docx está instalado
2. Si no, instálalo con pip3
3. Verifica la instalación
4. Vuelve a ejecutar el script
```

### Problema: Formato de Documento No Reconocido

```
El script no reconoce el formato de mi documento: ~/Downloads/nuevo.docx

Por favor:
1. Abre el documento y muéstrame las primeras 20 líneas
2. Identifica qué formato usa (Q1., Q1.1, otro)
3. Si es formato nuevo, ayúdame a modificar convert_survey.py para soportarlo
```

### Problema: JSON Incompleto

```
El JSON generado está incompleto (solo 1500 líneas vs 4000 esperadas)

Archivo: ~/Downloads/incompleto.json
Referencia: examples/completo.json

Por favor:
1. Compara ambos JSONs
2. Identifica qué falta
3. Corrige el problema
4. Regenera el JSON completo
```

### Problema: Git No Funciona

```
Tengo problemas con Git. Ayúdame a:
1. Verificar que git está instalado
2. Verificar que estoy autenticado con GitHub
3. Verificar que el remote está configurado
4. Hacer push de mis cambios
```

---

## PARTE 11: Comandos de Referencia Rápida

### Procesamiento Básico

```bash
# Comando directo (si prefieres ejecutar manualmente)
python3 ~/Documents/wpforms-survey-generator/convert_survey.py ~/Downloads/documento.docx
```

### Git

```bash
# Ver estado
git status

# Ver cambios
git diff

# Add, commit, push (Claude Code puede hacer esto por ti)
git add .
git commit -m "mensaje"
git push
```

### Python

```bash
# Verificar instalación
python3 --version
pip3 list | grep docx

# Reinstalar dependencia
pip3 install --upgrade python-docx
```

---

## PARTE 12: Flujo de Trabajo Completo - Ejemplo Real

### Escenario: Nueva Encuesta Coca-Cola para México

**Paso 1: Preparar**
```
Tengo nueva encuesta Coca-Cola para México:
- Documento: ~/Downloads/coca-mexico.docx
- Necesito versión en español con pesos mexicanos

Lee HISTORIA_CONVERSACION.md para ver formato de encuestas Coca-Cola anteriores.
```

**Paso 2: Procesar**
```
Procesa ~/Downloads/coca-mexico.docx:
1. Identifica formato (Q1. o Q1.1)
2. Detecta Likert Scales (busca tablas markdown)
3. Ejecuta convert_survey.py
4. Genera JSON completo en ~/Downloads/coca-mexico.json
```

**Paso 3: Verificar**
```
Verifica ~/Downloads/coca-mexico.json:
- ¿Cuántos campos tiene?
- ¿Cuántos Likert Scales?
- ¿Tienen todos columns y rows?
- ¿Estructura completa de WPForms?

Compara con examples/ para asegurar que está completo.
```

**Paso 4: Localizar**
```
Adapta ~/Downloads/coca-mexico.json para México:
- Income en pesos mexicanos (MXN)
- Regiones mexicanas: Ciudad de México, Norte, Centro, Sur, etc.
- Mantener nombres de productos Coca-Cola
- No cambiar tamaños de paquetes
- Traducir textos al español mexicano si es necesario

Genera: ~/Downloads/coca-mexico-final.json
```

**Paso 5: Validar**
```
Validación final de ~/Downloads/coca-mexico-final.json:
- Checklist completo de WPForms
- Todos los condicionales funcionan
- Likert Scales correctos
- No hay IDs duplicados
- No se usó ID 9

Dame reporte completo.
```

**Paso 6: Guardar Ejemplo**
```
Todo correcto. Por favor:
1. Copia coca-mexico-final.json a examples/
2. Actualiza HISTORIA_CONVERSACION.md mencionando esta encuesta
3. Commit con mensaje: "Add Coca-Cola México survey"
4. Push a GitHub
```

---

## PARTE 13: Ventajas de Usar Claude Code

### ✅ Ventajas vs Hacer Todo Manual

1. **Contexto Automático**: Claude Code lee HISTORIA_CONVERSACION.md automáticamente
2. **Validación Automática**: Verifica estructura completa sin que lo pidas
3. **Debugging Rápido**: Identifica y soluciona problemas al instante
4. **Iteración Rápida**: "Ajusta esto" y lo hace inmediatamente
5. **Git Integrado**: Commits y push automáticos con mensajes descriptivos
6. **Comparaciones**: Compara JSONs y documentos fácilmente
7. **Batch Processing**: Procesa múltiples documentos en un solo comando
8. **Aprendizaje**: Aprende de encuestas anteriores automáticamente

### ✅ Ventajas vs Cursor/Claude Project

1. **Todo en Uno**: No necesitas cambiar entre herramientas
2. **Terminal Integrado**: Ejecuta comandos y ve resultados en el mismo lugar
3. **Sin Configuración**: No necesitas setup de proyecto, solo empezar
4. **Conversacional**: Pides cambios en lenguaje natural
5. **Historial**: Puedes revisar conversaciones anteriores
6. **Sincronización**: Funciona desde cualquier lugar donde uses Claude Code

---

## PARTE 14: Best Practices

### 1. Siempre Valida Output

```
Después de cada procesamiento, pide:
"Valida el JSON generado contra estructura completa de WPForms"
```

### 2. Usa Referencias

```
"Usa el mismo formato que en HISTORIA_CONVERSACION.md"
"Copia la estructura de examples/brasil-reference.json"
```

### 3. Guarda Buenos Ejemplos

```
Cuando tengas un JSON perfecto:
"Guarda esto en examples/ para futuras referencias"
```

### 4. Commits Frecuentes

```
Después de cada cambio importante:
"Haz commit de estos cambios con mensaje descriptivo"
```

### 5. Documenta Problemas Nuevos

```
Si encuentras caso especial:
"Agrega nota sobre este caso a HISTORIA_CONVERSACION.md"
```

---

## PARTE 15: Checklist de Setup Completo

### ✅ Primera Vez en Nueva PC

- [ ] Claude Code instalado y funcionando
- [ ] Repositorio clonado: `~/Documents/wpforms-survey-generator`
- [ ] Python 3 instalado
- [ ] pip3 instalado
- [ ] python-docx instalado
- [ ] Git configurado y autenticado con GitHub
- [ ] Leído README.md y HISTORIA_CONVERSACION.md
- [ ] Probado con documento de ejemplo
- [ ] Verificado que genera JSON completo

### ✅ Para Cada Nueva Encuesta

- [ ] Documento en ~/Downloads/
- [ ] Identificar formato (Q1. o Q1.1)
- [ ] Procesar con convert_survey.py
- [ ] Verificar estructura completa
- [ ] Validar Likert Scales si los hay
- [ ] Crear versiones localizadas si es necesario
- [ ] Validar output final
- [ ] Guardar ejemplo si es relevante
- [ ] Commit y push si hay cambios al código

---

## PARTE 16: Resumen Rápido

### Para Procesar Encuesta Nueva (Mensaje Completo)

Copia y pega esto en Claude Code:

```
🎯 Nueva Encuesta para Procesar

Proyecto: ~/Documents/wpforms-survey-generator
Documento: ~/Downloads/[NOMBRE-DOCUMENTO].docx

CONTEXTO:
- Proyecto convierte Word a WPForms JSON
- Lee HISTORIA_CONVERSACION.md para entender encuestas anteriores
- Formato soportado: Q1. y Q1.1
- Tipos: Single choice, Multiple choice, Likert Scale, Open ended
- IMPORTANTE: ID 9 está reservado por WPForms (skip)

PASOS:
1. Analiza documento para identificar formato
2. Ejecuta: python3 convert_survey.py ~/Downloads/[NOMBRE-DOCUMENTO].docx
3. Verifica JSON generado tiene estructura COMPLETA de WPForms:
   - id, field_id, fields, settings, notifications, providers, etc.
4. Valida Likert Scales tengan columns y rows
5. Verifica no hay errores ni campos faltantes
6. Genera en: ~/Downloads/[NOMBRE]-final.json

VERSIONES LOCALIZADAS (si es necesario):
- UK: 8 regiones, income en £
- Brasil: 4 regiones, income en R$, portugués
- México: Regiones MX, income en MXN, español

VALIDACIÓN FINAL:
- Checklist completo WPForms
- Likert Scales correctos
- Condicionales funcionan
- No IDs duplicados

Procede con el procesamiento y avísame si hay algún problema.
```

---

## 🎉 ¡Todo Listo!

Ahora tienes todo lo necesario para trabajar con el proyecto usando Claude Code en tu nueva PC.

**Siguiente paso:**
1. Abre Claude Code
2. Clona el repo con el mensaje del Paso 2
3. Procesa tu primera encuesta con el prompt de la Parte 16

**Recuerda:**
- Claude Code hace todo automáticamente
- Solo necesitas pedirle lo que quieres en lenguaje natural
- Usa HISTORIA_CONVERSACION.md como referencia
- Valida siempre el output

---

**Repositorio:** https://github.com/mgazzera96/wpforms-survey-generator

**Todo el contexto está en los archivos del repo, Claude Code los leerá automáticamente cuando se lo pidas.**

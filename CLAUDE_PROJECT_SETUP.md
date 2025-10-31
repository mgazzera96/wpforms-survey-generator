# Configuración de Claude Project

Este documento explica cómo configurar el proyecto WPForms Survey Generator como un Claude Project para flujo de trabajo más simple.

## ¿Qué es un Claude Project?

Un Claude Project te permite tener conversaciones con contexto persistente sobre este proyecto específico, con acceso directo a todo el código y documentación.

## Pasos para Crear el Claude Project

### 1. Acceder a Claude.ai

1. Ve a https://claude.ai
2. Inicia sesión con tu cuenta
3. Busca la opción "Projects" en la barra lateral izquierda

### 2. Crear Nuevo Proyecto

1. Click en "Create Project" o "Nuevo Proyecto"
2. Nombre del proyecto: `WPForms Survey Generator`
3. Descripción: `Herramienta de conversión de documentos Word a JSON para formularios WPForms`

### 3. Agregar Conocimiento del Proyecto (Project Knowledge)

Agrega estos archivos como conocimiento base del proyecto:

**Archivos a incluir:**
- `README.md` - Documentación principal
- `HISTORIA_CONVERSACION.md` - Historial completo de desarrollo
- `convert_survey.py` - Código principal
- `examples/` - Ejemplos de conversiones anteriores
- `SETUP_NUEVA_PC.md` - Instrucciones de instalación

**Cómo agregar archivos:**
1. En la configuración del proyecto, busca "Project Knowledge" o "Conocimiento del Proyecto"
2. Haz click en "Add Files" o "Agregar Archivos"
3. Selecciona todos los archivos mencionados arriba
4. El contenido estará disponible en todas las conversaciones del proyecto

### 4. Configurar Instrucciones Personalizadas (Custom Instructions)

Agrega estas instrucciones para que Claude siempre entienda el contexto:

```
Eres un asistente especializado en el proyecto WPForms Survey Generator.

CONTEXTO:
- Esta aplicación convierte documentos Word (.docx) a JSON de WPForms
- Se han procesado múltiples encuestas: Heineken, Coca-Cola Dual (USA/UK/Brasil), BIC
- El formato de WPForms tiene estructura específica con campos, condicionales, y lógica
- El ID 9 está reservado por WPForms y debe saltarse

FORMATOS SOPORTADOS:
- Formato antiguo: Q1. Pregunta
- Formato nuevo: Q1.1 Pregunta
- Tipos: Single choice (→ Multiple Choice), Multiple selection (→ Checkboxes), Open ended (→ textarea)
- Tablas Likert en markdown dentro de documentos Word

COMPORTAMIENTO:
- Siempre mantener la estructura completa de WPForms (no generar versiones simplificadas)
- Usar templates de encuestas anteriores como base
- Al localizar para UK/Brasil, solo cambiar demografía (regiones, moneda), no tamaños de paquetes
- Verificar que Likert Scales tengan columns y rows correctos

UBICACIONES:
- Código: /Users/mateogazzera/Documents/wpforms-survey-generator/
- Documentos Word: Generalmente en Downloads
- Output JSONs: Downloads
```

### 5. Iniciar Primera Conversación

Una vez configurado el proyecto:

1. Abre el proyecto "WPForms Survey Generator"
2. Inicia una nueva conversación
3. Prueba con: "Dame un resumen del proyecto y las encuestas procesadas anteriormente"
4. Claude debería tener acceso a todo el contexto automáticamente

## Ventajas del Claude Project

✅ **Contexto Persistente**: Claude recuerda todo sobre el proyecto en cada conversación
✅ **Acceso a Archivos**: Puede referenciar código y documentación sin que los copies
✅ **Consistencia**: Mantiene el mismo comportamiento y estándares en todas las conversaciones
✅ **Historial**: Puedes revisar conversaciones anteriores del proyecto
✅ **Colaboración**: Otros usuarios pueden unirse al proyecto si lo compartes

## Uso Diario

### Para Procesar Nueva Encuesta:

1. Abre el proyecto en Claude.ai
2. Menciona: "Necesito procesar un nuevo documento: [nombre]"
3. Claude sabrá automáticamente:
   - Dónde está el código
   - Qué formato usar
   - Cómo manejar casos especiales
   - Estructura completa de WPForms

### Para Crear Versiones Localizadas:

1. Abre el proyecto en Claude.ai
2. Menciona: "Necesito versión UK/Brasil del JSON [nombre]"
3. Claude aplicará las reglas correctas de localización automáticamente

## Sincronización con GitHub

Si haces cambios en el código:

1. Pushea los cambios a GitHub
2. En Claude Project, actualiza los archivos en "Project Knowledge"
3. O simplemente menciona los cambios en la conversación

## Troubleshooting

**P: Claude no encuentra los archivos**
R: Verifica que agregaste los archivos en "Project Knowledge"

**P: Claude olvida el contexto**
R: Asegúrate de estar usando el proyecto específico, no chat general

**P: Necesito actualizar las instrucciones**
R: Ve a configuración del proyecto → Custom Instructions → Edita

## Próximos Pasos

1. ✅ Crear el proyecto en Claude.ai
2. ✅ Agregar todos los archivos a Project Knowledge
3. ✅ Configurar Custom Instructions
4. ✅ Probar con una encuesta simple
5. ✅ Usar para próximas conversiones

---

**Nota**: Esta es la forma más eficiente de trabajar con Claude para este proyecto. No necesitarás explicar el contexto cada vez.

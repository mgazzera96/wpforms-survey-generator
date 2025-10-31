# Configuración de Cursor IDE

Este documento explica cómo configurar el proyecto en Cursor IDE para desarrollo eficiente.

## ¿Qué es Cursor?

Cursor es un IDE basado en VS Code con integración de AI para coding. Permite trabajar con Claude directamente en el editor.

## Instalación de Cursor

### 1. Descargar e Instalar

1. Ve a https://cursor.sh
2. Descarga la versión para macOS
3. Instala arrastrando a Aplicaciones
4. Abre Cursor por primera vez

### 2. Configuración Inicial

**Importar Configuración de VS Code (Opcional):**
- Si usabas VS Code antes, Cursor puede importar tus configuraciones
- Settings → Import Settings from VS Code

## Configurar el Proyecto WPForms

### 1. Abrir el Proyecto

```bash
cd /Users/mateogazzera/Documents/wpforms-survey-generator
cursor .
```

O desde Cursor:
- File → Open Folder
- Selecciona `/Users/mateogazzera/Documents/wpforms-survey-generator`

### 2. Configurar Python

**Seleccionar Intérprete de Python:**

1. Presiona `Cmd+Shift+P`
2. Escribe: "Python: Select Interpreter"
3. Selecciona Python 3.x (el que instalaste)

**Verificar:**
- Terminal integrada: `` Ctrl+` ``
- Ejecuta: `python3 --version`
- Debería mostrar Python 3.x

### 3. Instalar Extensiones Recomendadas

**Extensiones esenciales:**

1. **Python** (Microsoft)
   - Sintaxis highlighting
   - Linting, debugging
   - IntelliSense

2. **Pylance** (Microsoft)
   - Type checking avanzado
   - Auto-completado mejorado

3. **GitLens** (opcional)
   - Visualización de git history
   - Blame annotations

**Instalar extensiones:**
- View → Extensions (o `Cmd+Shift+X`)
- Buscar cada extensión
- Click en "Install"

### 4. Configurar Workspace Settings

Crea `.vscode/settings.json` en el proyecto:

```json
{
  "python.defaultInterpreterPath": "/usr/local/bin/python3",
  "python.linting.enabled": true,
  "python.linting.pylintEnabled": false,
  "python.linting.flake8Enabled": true,
  "python.formatting.provider": "black",
  "editor.formatOnSave": true,
  "files.exclude": {
    "**/__pycache__": true,
    "**/*.pyc": true,
    "**/.DS_Store": true
  },
  "files.associations": {
    "*.json": "json"
  },
  "editor.rulers": [100],
  "editor.tabSize": 4,
  "editor.insertSpaces": true
}
```

### 5. Configurar AI de Cursor

**Activar Cursor AI:**

1. Presiona `Cmd+K` para abrir Cursor AI chat
2. O presiona `Cmd+L` para chat en panel lateral
3. Inicia sesión con tu cuenta de Cursor

**Configurar AI para el Proyecto:**

En el chat de Cursor AI, puedes decirle:
```
Este es un proyecto de conversión de Word a WPForms JSON.
Archivos principales:
- convert_survey.py: script principal
- HISTORIA_CONVERSACION.md: contexto completo del proyecto

Por favor familiarízate con el proyecto.
```

## Uso Diario de Cursor

### Comandos Útiles de AI

**1. Cmd+K - Inline AI Edit**
- Selecciona código
- Presiona `Cmd+K`
- Describe qué cambiar
- Ejemplo: "Add error handling for file not found"

**2. Cmd+L - AI Chat**
- Panel lateral de chat
- Pregunta sobre el código
- Ejemplo: "¿Cómo funciona el parser de Likert scales?"

**3. Cmd+I - Quick Question**
- Pregunta rápida sobre código seleccionado
- Ejemplo: Selecciona función → `Cmd+I` → "What does this do?"

### Flujo de Trabajo Típico

**Para modificar convert_survey.py:**

1. Abre `convert_survey.py`
2. Presiona `Cmd+L` para chat
3. Describe el cambio: "Necesito agregar soporte para formato Q1.a.1"
4. Cursor sugerirá cambios
5. Acepta o modifica según necesites

**Para debuggear:**

1. Click en número de línea para agregar breakpoint
2. Presiona `F5` para iniciar debugging
3. O usa terminal integrada para print debugging

**Para testing rápido:**

1. Abre terminal integrada (`` Ctrl+` ``)
2. Ejecuta: `python3 convert_survey.py ~/Downloads/documento.docx`
3. Revisa output

### Atajos de Teclado Importantes

| Atajo | Función |
|-------|---------|
| `Cmd+P` | Quick file open |
| `Cmd+Shift+P` | Command palette |
| `Cmd+B` | Toggle sidebar |
| `Cmd+K` | Inline AI edit |
| `Cmd+L` | AI chat panel |
| `` Ctrl+` `` | Toggle terminal |
| `Cmd+/` | Toggle comment |
| `Cmd+D` | Select next occurrence |
| `Option+↑/↓` | Move line up/down |
| `Option+Shift+↑/↓` | Copy line up/down |

## Integración con Git

### Panel de Source Control

1. Click en icono de Git en sidebar (o `Ctrl+Shift+G`)
2. Ve cambios en archivos
3. Stage cambios con `+`
4. Escribe mensaje de commit
5. Click en ✓ para commit

### Terminal Git

Puedes usar comandos git directamente en terminal integrada:

```bash
git status
git add .
git commit -m "mensaje"
git push
```

## Configuración del .cursorrules (Opcional)

Crea `.cursorrules` en el proyecto para instrucciones específicas a Cursor AI:

```
# WPForms Survey Generator Project Rules

## Context
This is a Word to WPForms JSON converter.

## Key Requirements
- Always maintain complete WPForms structure (id, field_id, fields, settings, etc.)
- Skip field ID 9 (reserved by WPForms)
- Support both Q1. and Q1.1 format
- Parse markdown tables for Likert scales

## Code Style
- Python 3.x
- 4 spaces indentation
- Descriptive variable names
- Comments in Spanish for user-facing messages

## Testing
- Always test with example documents in examples/ folder
- Verify output has all WPForms required fields
- Check Likert scales have columns and rows

## Localization
- UK: 8 regions, income in £
- Brasil: 4 regions, income in R$, Portuguese translation
- Only change demographics, not product info
```

## Tips para Usar Cursor Eficientemente

### 1. Context Awareness
- Cursor AI puede ver archivos abiertos
- Abre archivos relevantes antes de preguntar
- Usa `@filename` en chat para referenciar archivos específicos

### 2. Multi-file Edits
- Cursor puede sugerir cambios en múltiples archivos
- Útil para refactoring grande

### 3. Terminal Integrada
- Usa terminal integrada en lugar de terminal externa
- Cursor AI puede ver output de terminal
- Útil para debugging

### 4. Snippets
- Crea snippets para código repetitivo
- File → Preferences → User Snippets

### 5. AI Composer
- Para cambios grandes en múltiples archivos
- `Cmd+Shift+I` para abrir composer
- Describe cambio complejo, Cursor genera plan

## Troubleshooting

### Python no se encuentra
```bash
# Verifica instalación
which python3

# En Cursor, actualiza interpreter path
Cmd+Shift+P → Python: Select Interpreter
```

### AI no responde
- Verifica conexión a internet
- Verifica que estés logueado en Cursor
- Reinicia Cursor

### Extensiones no funcionan
- Reload window: `Cmd+Shift+P` → "Reload Window"
- Reinstala extensión

### Terminal no abre
- `` Ctrl+` `` toggle terminal
- O View → Terminal

## Flujo de Trabajo Completo: Nueva Encuesta

1. **Recibir documento Word**
   ```bash
   # Documento en ~/Downloads/nueva-encuesta.docx
   ```

2. **Abrir proyecto en Cursor**
   ```bash
   cd ~/Documents/wpforms-survey-generator
   cursor .
   ```

3. **Revisar formato del documento**
   - Usar `Cmd+L` para preguntar a AI
   - "¿Este documento usa formato Q1. o Q1.1?"

4. **Ejecutar conversión**
   ```bash
   python3 convert_survey.py ~/Downloads/nueva-encuesta.docx
   ```

5. **Revisar output**
   - Abrir JSON generado
   - Verificar estructura con AI:
     - `Cmd+L`: "¿Este JSON tiene todos los campos requeridos de WPForms?"

6. **Hacer ajustes si necesario**
   - Seleccionar código a modificar
   - `Cmd+K`: describir cambio
   - Probar nuevamente

7. **Commit cambios**
   - Source Control panel
   - Stage, commit, push

## Próximos Pasos

1. ✅ Instalar Cursor
2. ✅ Abrir proyecto
3. ✅ Configurar Python
4. ✅ Instalar extensiones
5. ✅ Crear .cursorrules
6. ✅ Probar con documento de ejemplo

---

**Nota**: Cursor AI es extremadamente útil para este proyecto. Puede entender la estructura de WPForms y ayudar con debugging rápido.

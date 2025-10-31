# Guía Completa de Migración a Nueva PC

Esta guía consolida todos los pasos para migrar el proyecto WPForms Survey Generator a tu nueva computadora.

## Resumen Rápido

1. **En esta PC (actual)**: Subir proyecto a GitHub
2. **En nueva PC**: Clonar proyecto, instalar dependencias, configurar herramientas
3. **Configuración**: Cursor IDE + Claude Project
4. **Verificación**: Probar con encuesta de ejemplo

---

## PARTE 1: Preparación en PC Actual

### ✅ Ya Completado

- [x] Git inicializado
- [x] .gitignore creado
- [x] Commits iniciales realizados
- [x] Documentación completa

### Paso 1: Verificar Estado del Repositorio

```bash
cd /Users/mateogazzera/Documents/wpforms-survey-generator
git status
```

**Deberías ver**: "On branch main, nothing to commit, working tree clean"

### Paso 2: Crear Repositorio en GitHub

1. Ve a https://github.com
2. Click en "+" → "New repository"
3. **Nombre**: `wpforms-survey-generator`
4. **Descripción**: `Word to WPForms JSON converter - Cuestionarios marketing`
5. **Privado o Público**: Elige según prefieras
6. **NO** inicialices con README (ya tienes uno)
7. Click "Create repository"

### Paso 3: Conectar Repositorio Local a GitHub

GitHub te mostrará comandos. Usa estos:

```bash
cd /Users/mateogazzera/Documents/wpforms-survey-generator

# Agregar remote
git remote add origin https://github.com/TU-USUARIO/wpforms-survey-generator.git

# Verificar que se agregó
git remote -v

# Push inicial
git branch -M main
git push -u origin main
```

**Reemplaza `TU-USUARIO`** con tu nombre de usuario de GitHub.

### Paso 4: Verificar Subida

1. Refresca la página de GitHub
2. Deberías ver todos los archivos:
   - convert_survey.py
   - README.md
   - HISTORIA_CONVERSACION.md
   - SETUP_NUEVA_PC.md
   - INSTRUCCIONES_GITHUB.md
   - CLAUDE_PROJECT_SETUP.md
   - CURSOR_SETUP.md
   - MIGRACION_COMPLETA.md
   - examples/
   - docs/

---

## PARTE 2: Configuración en Nueva PC

### Paso 1: Instalar Prerequisitos

**1. Instalar Homebrew (si no está instalado)**

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

**2. Instalar Python 3**

```bash
brew install python3
python3 --version  # Verificar: debe ser 3.x
```

**3. Instalar Git (si no está instalado)**

```bash
brew install git
git --version  # Verificar instalación
```

### Paso 2: Clonar Repositorio

```bash
# Ir a Documents
cd ~/Documents

# Clonar proyecto
git clone https://github.com/TU-USUARIO/wpforms-survey-generator.git

# Entrar al directorio
cd wpforms-survey-generator

# Verificar archivos
ls -la
```

### Paso 3: Instalar Dependencias Python

```bash
pip3 install python-docx

# Verificar instalación
python3 -c "import docx; print('✓ python-docx instalado correctamente')"
```

### Paso 4: Probar Aplicación

**Usa uno de los ejemplos incluidos:**

```bash
# Listar ejemplos disponibles
ls examples/

# Probar conversión con ejemplo
python3 convert_survey.py examples/ejemplo-simple.docx

# Debería generar JSON en el mismo directorio
```

Si no hay ejemplos, puedes crear un documento de prueba simple:

```bash
# Crear documento de prueba básico
cat > test-survey.txt << 'EOF'
Q1. Gender
→ Single choice
Male
Female

Q2. Age
→ Single choice
18-25
26-35
36-45
46+
EOF

# Convertir a docx usando textutil (macOS)
textutil -convert docx test-survey.txt

# Probar conversión
python3 convert_survey.py test-survey.docx
```

---

## PARTE 3: Configurar Cursor IDE

### Paso 1: Descargar e Instalar

1. Ve a https://cursor.sh
2. Descarga para macOS
3. Arrastra a Aplicaciones
4. Abre Cursor

### Paso 2: Abrir Proyecto

**Desde terminal:**
```bash
cd ~/Documents/wpforms-survey-generator
cursor .
```

**Desde Cursor:**
- File → Open Folder
- Selecciona `~/Documents/wpforms-survey-generator`

### Paso 3: Configurar Python en Cursor

1. `Cmd+Shift+P`
2. Escribe: "Python: Select Interpreter"
3. Selecciona Python 3.x

### Paso 4: Instalar Extensiones

**Extensiones recomendadas:**
- Python (Microsoft)
- Pylance (Microsoft)
- GitLens (opcional)

**Instalar:**
- `Cmd+Shift+X` para abrir Extensions
- Buscar e instalar cada una

### Paso 5: Crear Configuración de Workspace

Cursor debería detectar el proyecto Python automáticamente, pero puedes crear `.vscode/settings.json`:

```bash
mkdir -p .vscode
cat > .vscode/settings.json << 'EOF'
{
  "python.defaultInterpreterPath": "/usr/local/bin/python3",
  "editor.formatOnSave": true,
  "files.exclude": {
    "**/__pycache__": true,
    "**/*.pyc": true,
    "**/.DS_Store": true
  }
}
EOF
```

**Ver documentación completa en**: `CURSOR_SETUP.md`

---

## PARTE 4: Configurar Claude Project

### Paso 1: Crear Proyecto en Claude.ai

1. Ve a https://claude.ai
2. Inicia sesión
3. Click en "Projects" (barra lateral)
4. Click "Create Project"

### Paso 2: Configurar Proyecto

**Información básica:**
- **Nombre**: `WPForms Survey Generator`
- **Descripción**: `Conversor de encuestas Word a WPForms JSON`

### Paso 3: Agregar Project Knowledge

**Archivos a subir:**

En la sección "Project Knowledge":
1. Click "Add Files"
2. Selecciona estos archivos desde `~/Documents/wpforms-survey-generator`:
   - `README.md`
   - `HISTORIA_CONVERSACION.md`
   - `convert_survey.py`
   - `SETUP_NUEVA_PC.md`
   - Archivos de `examples/` (si tienes)

### Paso 4: Custom Instructions

En la configuración del proyecto, agrega estas instrucciones:

```
Eres un asistente especializado en WPForms Survey Generator.

CONTEXTO DEL PROYECTO:
- Convierte documentos Word (.docx) a JSON de WPForms
- Encuestas procesadas: Heineken, Coca-Cola Dual (USA/UK/Brasil), BIC
- Soporte para formatos: Q1. y Q1.1
- Tipos: Single choice, Multiple selection, Open ended, Likert Scale

REGLAS IMPORTANTES:
1. ID 9 está reservado por WPForms (skip en counter)
2. Siempre generar estructura COMPLETA de WPForms
3. No simplificar o omitir campos requeridos
4. Usar templates de encuestas anteriores como referencia

LOCALIZACION:
- UK: 8 regiones, income en £
- Brasil: 4 regiones, income en R$, traducción al portugués
- Solo cambiar demografía (regiones, moneda)
- NO cambiar: tamaños de paquetes, nombres de productos

UBICACIONES:
- Proyecto: ~/Documents/wpforms-survey-generator/
- Docs Word: Generalmente ~/Downloads/
- Output: ~/Downloads/

FLUJO DE TRABAJO:
1. Usuario proporciona documento Word
2. Identificar formato (Q1. vs Q1.1)
3. Ejecutar convert_survey.py
4. Verificar output (estructura completa, Likert scales correctos)
5. Si necesario, crear versiones localizadas
```

### Paso 5: Probar Claude Project

1. Abre el proyecto en Claude.ai
2. Prueba: "Dame un resumen de las encuestas procesadas anteriormente"
3. Claude debería responder con contexto del proyecto

**Ver documentación completa en**: `CLAUDE_PROJECT_SETUP.md`

---

## PARTE 5: Flujo de Trabajo en Nueva PC

### Para Procesar Nueva Encuesta

**Opción 1: Usando Cursor + Terminal**

```bash
# 1. Documento debe estar en Downloads
# Ejemplo: ~/Downloads/nueva-encuesta.docx

# 2. Abrir proyecto en Cursor
cd ~/Documents/wpforms-survey-generator
cursor .

# 3. Ejecutar conversión
python3 convert_survey.py ~/Downloads/nueva-encuesta.docx

# 4. Output estará en Downloads
open ~/Downloads/  # Ver JSON generado
```

**Opción 2: Usando Claude Project**

1. Abre proyecto en https://claude.ai
2. Mensaje: "Necesito procesar ~/Downloads/nueva-encuesta.docx"
3. Claude ejecutará comandos y verificará output
4. Te dirá si hay problemas o ajustes necesarios

### Para Crear Versiones Localizadas

**En Claude Project:**

```
Tengo el JSON USA final: ~/Downloads/encuesta-usa-final.json
Necesito versiones para:
- UK (8 regiones, £)
- Brasil (4 regiones, R$, portugués)
```

Claude creará ambas versiones automáticamente.

### Para Hacer Cambios al Código

**En Cursor:**

1. Abre `convert_survey.py`
2. `Cmd+L` para AI chat
3. Describe cambio: "Necesito agregar soporte para tipo de pregunta X"
4. Cursor sugerirá cambios
5. Prueba con documento de ejemplo
6. Commit:
   ```bash
   git add convert_survey.py
   git commit -m "Add support for question type X"
   git push
   ```

---

## PARTE 6: Checklist de Migración

### ✅ En PC Actual

- [ ] Verificar git status limpio
- [ ] Crear repositorio en GitHub
- [ ] Conectar remote: `git remote add origin URL`
- [ ] Push: `git push -u origin main`
- [ ] Verificar archivos en GitHub web

### ✅ En Nueva PC - Instalación

- [ ] Instalar Homebrew
- [ ] Instalar Python 3: `brew install python3`
- [ ] Instalar Git: `brew install git`
- [ ] Clonar repo: `git clone URL`
- [ ] Instalar dependencias: `pip3 install python-docx`
- [ ] Probar: `python3 convert_survey.py ejemplo.docx`

### ✅ En Nueva PC - Cursor

- [ ] Descargar Cursor de cursor.sh
- [ ] Instalar en Aplicaciones
- [ ] Abrir proyecto: `cursor ~/Documents/wpforms-survey-generator`
- [ ] Configurar Python interpreter
- [ ] Instalar extensiones: Python, Pylance
- [ ] Probar terminal integrada
- [ ] Crear .cursorrules (opcional)

### ✅ En Nueva PC - Claude Project

- [ ] Ir a claude.ai
- [ ] Crear nuevo proyecto
- [ ] Agregar archivos a Project Knowledge
- [ ] Configurar Custom Instructions
- [ ] Probar con mensaje test
- [ ] Verificar que tiene contexto completo

### ✅ Verificación Final

- [ ] Procesar encuesta de ejemplo end-to-end
- [ ] Verificar JSON output completo
- [ ] Crear versión localizada (UK o Brasil)
- [ ] Hacer cambio pequeño al código
- [ ] Commit y push a GitHub
- [ ] Pull desde PC actual para verificar sincronización

---

## PARTE 7: Comandos de Referencia Rápida

### Git

```bash
# Ver estado
git status

# Ver cambios
git diff

# Agregar cambios
git add .

# Commit
git commit -m "mensaje"

# Push
git push

# Pull (obtener cambios de GitHub)
git pull

# Ver historial
git log --oneline
```

### Python

```bash
# Ejecutar script
python3 convert_survey.py documento.docx

# Verificar instalación
python3 --version
pip3 list | grep docx

# Reinstalar dependencia
pip3 install --upgrade python-docx
```

### Cursor

```bash
# Abrir proyecto
cursor ~/Documents/wpforms-survey-generator

# O desde dentro del directorio
cd ~/Documents/wpforms-survey-generator
cursor .
```

**Atajos en Cursor:**
- `Cmd+K`: AI inline edit
- `Cmd+L`: AI chat
- `Cmd+P`: Quick file open
- `` Ctrl+` ``: Toggle terminal

---

## PARTE 8: Troubleshooting

### Problema: python-docx no se encuentra

```bash
# Reinstalar
pip3 install python-docx

# O con flag para usuario específico
pip3 install --user python-docx

# Verificar
python3 -c "import docx; print('OK')"
```

### Problema: Git push falla (autenticación)

```bash
# Necesitas configurar GitHub authentication
# Opción 1: SSH key (recomendado)
ssh-keygen -t ed25519 -C "tu@email.com"
cat ~/.ssh/id_ed25519.pub  # Copiar y agregar a GitHub

# Opción 2: Personal access token
# GitHub → Settings → Developer settings → Personal access tokens
# Crear token y usarlo como password
```

### Problema: Cursor no encuentra Python

1. `Cmd+Shift+P`
2. "Python: Select Interpreter"
3. Si no aparece, instalar: `brew install python3`
4. Reload Cursor

### Problema: Claude Project no tiene contexto

- Verificar que agregaste archivos en "Project Knowledge"
- Archivos grandes pueden tardar en procesarse
- Intenta referenciar archivo específico: "@README.md what is this project?"

---

## PARTE 9: Siguiente Trabajo

Una vez todo configurado, estarás listo para:

1. **Procesar encuestas nuevas** desde nueva PC
2. **Crear versiones localizadas** rápidamente
3. **Hacer mejoras al código** con ayuda de Cursor AI
4. **Mantener historial** completo en Git/GitHub
5. **Consultar contexto** en Claude Project cuando necesites

### Primera Tarea Recomendada

Procesa una encuesta de prueba end-to-end:

1. Crea documento simple en ~/Downloads/test.docx:
   ```
   Q1. Test question
   → Single choice
   Option 1
   Option 2
   ```

2. Procesa:
   ```bash
   python3 convert_survey.py ~/Downloads/test.docx
   ```

3. Verifica JSON output

4. Pregunta a Claude Project:
   ```
   "¿El JSON generado tiene la estructura correcta de WPForms?"
   ```

---

## Recursos

- **Documentación del proyecto**: README.md
- **Historial completo**: HISTORIA_CONVERSACION.md
- **Setup detallado**: SETUP_NUEVA_PC.md
- **GitHub**: INSTRUCCIONES_GITHUB.md
- **Cursor**: CURSOR_SETUP.md
- **Claude Project**: CLAUDE_PROJECT_SETUP.md

---

## Resumen de Ubicaciones

```
Nueva PC:
~/Documents/wpforms-survey-generator/     ← Proyecto principal
~/Downloads/                               ← Documentos Word de entrada
~/Downloads/                               ← JSONs de salida

GitHub:
https://github.com/TU-USUARIO/wpforms-survey-generator

Claude:
https://claude.ai → Projects → WPForms Survey Generator

Cursor:
Abierto en ~/Documents/wpforms-survey-generator
```

---

**¡Listo para migrar!** Sigue los pasos en orden y tendrás todo funcionando en la nueva PC.

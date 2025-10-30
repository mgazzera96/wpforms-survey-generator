# 🚀 Instrucciones para Subir a GitHub y Migrar a Nueva PC

## 📍 ESTÁS AQUÍ (Mac Actual)

El repositorio Git ya está inicializado y con el commit inicial hecho.

---

## PASO 1: Crear Repositorio en GitHub

### Opción A: Desde el Navegador (Más Fácil)

1. Ve a https://github.com
2. Click en el botón **"+"** arriba a la derecha → **"New repository"**
3. Configuración:
   - **Repository name:** `wpforms-survey-generator`
   - **Description:** `Convertidor de Word a JSON para WPForms - Generado con Claude Code`
   - **Visibility:** Private o Public (tu elección)
   - ❌ **NO** marcar "Add a README file"
   - ❌ **NO** marcar "Add .gitignore"
   - ❌ **NO** seleccionar license
4. Click **"Create repository"**

### Opción B: Desde CLI (con gh)

```bash
# Si tenés GitHub CLI instalado
gh repo create wpforms-survey-generator --private --source=. --remote=origin --push
```

---

## PASO 2: Conectar Repo Local con GitHub

Después de crear el repo en GitHub, verás una pantalla con comandos. Usá estos:

```bash
cd ~/Documents/wpforms-survey-generator

# Agregar remote de GitHub (reemplazá TU_USUARIO con tu usuario de GitHub)
git remote add origin https://github.com/TU_USUARIO/wpforms-survey-generator.git

# O si usás SSH:
# git remote add origin git@github.com:TU_USUARIO/wpforms-survey-generator.git

# Verificar que se agregó
git remote -v
```

---

## PASO 3: Push a GitHub

```bash
cd ~/Documents/wpforms-survey-generator

# Push del código
git push -u origin main

# Si te pide credenciales:
# - Usuario: tu_usuario_github
# - Password: usa un Personal Access Token (PAT), NO tu password de GitHub
```

### Crear Personal Access Token (si es necesario):
1. GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Generate new token
3. Scopes: marcar `repo`
4. Copiar el token y usarlo como password

---

## PASO 4: Verificar en GitHub

1. Ve a `https://github.com/TU_USUARIO/wpforms-survey-generator`
2. Deberías ver:
   - ✅ convert_survey.py
   - ✅ README.md
   - ✅ HISTORIA_CONVERSACION.md
   - ✅ SETUP_NUEVA_PC.md
   - ✅ docs/
   - ✅ examples/

---

## PASO 5: En Tu Nueva PC

### 5.1 Instalar Requisitos

```bash
# Instalar Python (si no está)
# macOS:
brew install python

# Verificar
python3 --version
```

### 5.2 Clonar el Repositorio

```bash
# Ir a Documents
cd ~/Documents

# Clonar (reemplazá TU_USUARIO)
git clone https://github.com/TU_USUARIO/wpforms-survey-generator.git

# Entrar
cd wpforms-survey-generator
```

### 5.3 Instalar Dependencias

```bash
pip3 install python-docx
```

### 5.4 Probar que Funciona

```bash
# Ver ayuda
python3 convert_survey.py

# Deberías ver:
# Uso: python3 convert_survey.py archivo.docx [salida.json]
```

---

## PASO 6: Copiar Archivos Grandes (No están en Git)

Los archivos `.docx` y `.json` grandes NO están en Git. Necesitás copiarlos manualmente:

### Archivos a Copiar Manualmente:

**Desde Mac Actual:**
```
/Users/mateogazzera/Downloads/
├── coca-cola-dual-brasil-survey.json (134 KB)
├── coca-cola-dual-uk-survey-FINAL.json (130 KB)
├── coca-cola-dual-usa-survey.json (37 KB)
├── coca-cola-dual-vf-VERSION-FINALIZADA.json (115 KB) ⭐
├── bic-afeitadoras-ar-survey-FINAL-CONDICIONALES.json
├── Coca Dual VF.docx ⭐ IMPORTANTE
├── Coca Cola Dual.docx
└── BIC Afeitadoras.docx
```

**Métodos para Copiar:**
1. **USB/Disco Externo**
2. **AirDrop** (entre Macs)
3. **Google Drive / Dropbox**
4. **iCloud Drive**

**A Nueva PC:**
```
/Users/TU_USUARIO/Downloads/
```

---

## PASO 7: Verificar Todo en Nueva PC

```bash
cd ~/Documents/wpforms-survey-generator

# Test 1: Python funciona
python3 --version

# Test 2: python-docx instalado
python3 -c "from docx import Document; print('✅ OK')"

# Test 3: Procesar un archivo
python3 convert_survey.py ~/Downloads/"Coca Dual VF.docx" ~/Downloads/test-output.json

# Test 4: Verificar que se generó
ls -lh ~/Downloads/test-output.json
```

---

## PASO 8: Abrir en Cursor/VS Code

```bash
# Opción 1: Cursor
cursor ~/Documents/wpforms-survey-generator

# Opción 2: VS Code
code ~/Documents/wpforms-survey-generator
```

---

## 📋 CHECKLIST COMPLETO

### En Mac Actual:
- [x] Git inicializado
- [x] Commit inicial hecho
- [ ] Crear repo en GitHub
- [ ] Push a GitHub
- [ ] Copiar archivos grandes a USB/Drive

### En Nueva PC:
- [ ] Clonar repo desde GitHub
- [ ] Instalar python-docx
- [ ] Copiar archivos grandes desde USB/Drive
- [ ] Probar convert_survey.py
- [ ] Leer HISTORIA_CONVERSACION.md
- [ ] Leer SETUP_NUEVA_PC.md

---

## 🆘 Si Algo Falla

1. **Error al push:** Verificá que el remote esté bien configurado
   ```bash
   git remote -v
   ```

2. **Error de autenticación:** Usá Personal Access Token, no password

3. **Error en nueva PC:** Revisá que python-docx esté instalado
   ```bash
   pip3 list | grep docx
   ```

4. **Archivo no procesa:** Verificá que el .docx esté en la ubicación correcta

---

## 📞 CONTEXTO COMPLETO

Lee estos archivos en orden para entender todo:

1. **README.md** - Overview general
2. **HISTORIA_CONVERSACION.md** - Todo lo que hicimos ⭐
3. **SETUP_NUEVA_PC.md** - Setup detallado
4. **docs/field-types.md** - Tipos de campos
5. **docs/reverse-engineering-met4u.md** - Ejemplo de encuesta compleja

---

**¡Listo!** Con esto tenés todo documentado para migrar sin perder contexto.

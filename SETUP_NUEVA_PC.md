# 🖥️ Setup en Nueva Computadora

## 📋 Requisitos Previos

1. **Python 3.x** instalado
2. **Git** instalado
3. **Cuenta de GitHub** (si aún no tenés)

---

## 🚀 PASOS PARA NUEVA PC

### 1. Clonar el Repositorio

```bash
# Ir a tu carpeta de proyectos
cd ~/Documents

# Clonar el repo
git clone https://github.com/TU_USUARIO/wpforms-survey-generator.git

# Entrar a la carpeta
cd wpforms-survey-generator
```

### 2. Instalar Dependencias

```bash
# Instalar python-docx
pip3 install python-docx

# O con --user si es necesario
pip3 install --user python-docx

# O con homebrew en macOS
brew install python
pip3 install python-docx
```

### 3. Verificar Instalación

```bash
# Probar que funciona
python3 convert_survey.py

# Deberías ver:
# Uso: python3 convert_survey.py archivo.docx [salida.json]
```

### 4. Configurar en Cursor/VS Code

```bash
# Abrir en Cursor
cursor ~/Documents/wpforms-survey-generator

# O abrir en VS Code
code ~/Documents/wpforms-survey-generator
```

---

## 📖 CÓMO USAR LA APP

### Uso Básico

```bash
python3 convert_survey.py "archivo.docx" "salida.json"
```

### Ejemplos

```bash
# Ejemplo 1: Convertir Coca-Cola survey
python3 convert_survey.py ~/Downloads/"Coca Dual VF.docx" ~/Downloads/output.json

# Ejemplo 2: Con ruta relativa
python3 convert_survey.py "./input/survey.docx" "./output/survey.json"

# Ejemplo 3: Auto-nombrar salida
python3 convert_survey.py "encuesta.docx"
# Genera: encuesta.json
```

---

## 🧪 PROBAR QUE TODO FUNCIONA

### Test 1: Verificar Python

```bash
python3 --version
# Debería mostrar: Python 3.x.x
```

### Test 2: Verificar python-docx

```bash
python3 -c "from docx import Document; print('✅ python-docx funciona')"
# Debería mostrar: ✅ python-docx funciona
```

### Test 3: Procesar Archivo de Ejemplo

```bash
# Si hay archivos en examples/
cd ~/Documents/wpforms-survey-generator
python3 convert_survey.py examples/ejemplo.docx output-test.json

# Verificar que se generó el JSON
ls -lh output-test.json
```

---

## 📂 ESTRUCTURA DEL PROYECTO

```
wpforms-survey-generator/
├── README.md                     # Documentación general
├── HISTORIA_CONVERSACION.md      # Resumen de todo el trabajo
├── SETUP_NUEVA_PC.md            # Esta guía
├── convert_survey.py            # Script principal ⭐
├── .gitignore                   # Archivos ignorados por git
├── examples/                    # Ejemplos de JSONs generados
│   ├── coca-cola-survey.json
│   └── heineken-survey.json
└── docs/                        # Documentación adicional
    ├── field-types.md
    └── reverse-engineering-met4u.md
```

---

## 🔧 TROUBLESHOOTING

### Error: "python-docx not installed"

```bash
pip3 install --user python-docx

# Si sigue fallando
pip3 install --break-system-packages python-docx
```

### Error: "Permission denied"

```bash
# Hacer el script ejecutable
chmod +x convert_survey.py

# Luego ejecutar
./convert_survey.py archivo.docx
```

### Error: "File not found"

```bash
# Verificar que el archivo existe
ls -la ~/Downloads/*.docx

# Usar ruta absoluta
python3 convert_survey.py "/Users/TU_USUARIO/Downloads/archivo.docx" output.json
```

---

## 📞 CONTEXTO HISTÓRICO

Esta app fue desarrollada en múltiples sesiones con Claude Code:

- **Sep 2025:** Versión inicial para Coca-Cola/Heineken
- **Oct 13, 2025:** MET4U con condicionales complejos
- **Oct 23, 2025:** BIC + Coca-Cola Dual (Brasil/UK/USA)
- **Oct 30, 2025:** Coca-Cola VF con nuevo formato

Todos los JSONs generados exitosamente están documentados en `HISTORIA_CONVERSACION.md`.

---

## 🎯 SIGUIENTE PASO

Una vez que todo funcione en la nueva PC:

1. ✅ Verificar que `python3 convert_survey.py` funciona
2. ✅ Probar con un archivo de ejemplo
3. ✅ Leer `HISTORIA_CONVERSACION.md` para entender todo el contexto
4. ✅ Continuar procesando nuevas encuestas

---

## 💾 BACKUP DE ARCHIVOS IMPORTANTES

Los archivos `.docx` originales y `.json` generados NO están en Git (son muy grandes).

**IMPORTANTE:** Antes de migrar, asegurate de copiar manualmente:
- `/Users/mateogazzera/Downloads/coca-cola-dual-*.json`
- `/Users/mateogazzera/Downloads/bic-*.json`
- `/Users/mateogazzera/Downloads/*.docx` (archivos Word originales)

Podés copiarlos a un USB, Google Drive, o Dropbox.

---

**¿Todo claro?** Si algo no funciona, revisá `HISTORIA_CONVERSACION.md` para ver cómo se resolvieron problemas similares antes.

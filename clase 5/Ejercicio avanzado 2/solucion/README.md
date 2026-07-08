# Solucion - Ejercicio avanzado 2

## Contenido

Esta carpeta deja una version completa y auto-contenida de lo que se espera para el ejercicio:

- API local por ambientes;
- app Streamlit;
- archivos `.env` de ejemplo;
- dataset por ambiente.

## Como probarla

### 1. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 2. Levantar la API

```bash
python service.py
```

### 3. Crear archivos `.env`

```bash
cp .env.development.example .env.development
cp .env.staging.example .env.staging
cp .env.production.example .env.production
```

### 4. Levantar Streamlit

```bash
streamlit run streamlit_app.py
```

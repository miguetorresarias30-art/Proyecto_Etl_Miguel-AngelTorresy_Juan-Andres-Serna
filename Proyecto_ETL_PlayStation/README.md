<<<<<<< HEAD
# 🎮 Proyecto ETL — Videojuegos de PlayStation

**Integrantes:** Miguel Angel Torres y Juan Andres Serna  
**Tema:** Análisis y procesamiento de datos de videojuegos de PlayStation  
**Asignatura:** Extracción, Transformación y Carga de Datos (ETL)

## 1. Objetivo

Construir un pipeline ETL de extremo a extremo que permita extraer datos de videojuegos, identificar problemas de calidad, limpiar y estandarizar los registros y finalmente cargarlos en una base de datos SQLite.

## 2. Flujo

```text
CSV de videojuegos
       ↓
   EXTRACCIÓN
 lectura por lotes + filtro PlayStation
       ↓
 TRANSFORMACIÓN
 perfilación + limpieza + estandarización
 + conversión de tipos + eliminación de duplicados
       ↓
       CARGA
   SQLite (playstation_etl.db)
       ↓
 reporte de calidad + logs
```

## 3. Estructura

```text
Proyecto_ETL_PlayStation/
├── data/
│   ├── raw/
│   │   └── videojuegos_playstation.csv
│   ├── processed/
│   └── README.md
├── logs/
├── reports/
├── src/
│   ├── __init__.py
│   ├── extract.py
│   ├── transform.py
│   └── load.py
├── .gitignore
├── main.py
└── requirements.txt
```

## 4. Problemas de calidad trabajados

- Valores nulos.
- Duplicados.
- Espacios innecesarios.
- Diferencias de mayúsculas/minúsculas en categorías.
- Valores `tbd` en puntuaciones.
- Conversión de columnas numéricas.
- Categorías desconocidas.
- Validación básica del año.

## 5. Instalación

Crear un entorno virtual:

```bash
python -m venv .venv
```

Activarlo en Windows:

```bash
.venv\Scripts\activate
```

Instalar dependencias:

```bash
pip install -r requirements.txt
```

## 6. Ejecución

Desde la raíz del proyecto:

```bash
python main.py
```

El pipeline genera:

- `data/processed/playstation_etl.db`
- `reports/quality_report.json`
- `logs/etl.log`

## 7. Resultado esperado

La base SQLite contiene una tabla llamada `games` con los registros transformados. El proceso es idempotente porque la carga reconstruye la tabla de destino en cada ejecución, evitando que una segunda ejecución acumule duplicados.

## 8. Herramientas

- Python
- Pandas
- NumPy
- SQLite
- SQLAlchemy
- GitHub
- Visual Studio Code

## 9. Fuente de datos

El conjunto de trabajo se basa en un dataset público de ventas de videojuegos que contiene nombre, plataforma, año, género, editor y ventas regionales/globales. Para este proyecto se trabaja específicamente con plataformas PlayStation.
# Proyecto_Etl_Miguel-AngelTorresy_Juan-Andres-Serna
>>>>>>> 7b8a1fc788b9ad1e08eff3cf97c65caa1c3238ed

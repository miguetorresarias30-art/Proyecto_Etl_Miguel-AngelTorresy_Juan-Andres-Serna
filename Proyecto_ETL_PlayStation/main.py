import json
import logging
from pathlib import Path

from src.extract import extract_data
from src.transform import transform_data
from src.load import load_to_sqlite

ROOT = Path(__file__).resolve().parent
RAW = ROOT / "data" / "raw" / "videojuegos_playstation.csv"
DB = ROOT / "data" / "processed" / "playstation_etl.db"
REPORT = ROOT / "reports" / "quality_report.json"
LOG_DIR = ROOT / "logs"

LOG_DIR.mkdir(exist_ok=True)
logging.basicConfig(
    filename=LOG_DIR / "etl.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

def main():
    logging.info("Inicio del pipeline ETL")

    extracted = extract_data(RAW, chunksize=1000)
    logging.info("Extracción completada: %s registros", len(extracted))

    transformed, report = transform_data(extracted)
    REPORT.write_text(json.dumps(report, indent=4, ensure_ascii=False), encoding="utf-8")
    logging.info("Transformación completada: %s registros", len(transformed))

    load_to_sqlite(transformed, DB)
    logging.info("Carga completada en %s", DB)

    print("ETL ejecutado correctamente.")
    print(f"Registros extraídos: {len(extracted)}")
    print(f"Registros cargados: {len(transformed)}")
    print(f"Base de datos: {DB}")
    print(f"Reporte: {REPORT}")

if __name__ == "__main__":
    main()

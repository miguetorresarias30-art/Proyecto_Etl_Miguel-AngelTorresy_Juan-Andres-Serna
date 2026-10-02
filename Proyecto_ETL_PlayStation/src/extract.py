import pandas as pd
from pathlib import Path

PLAYSTATION_PLATFORMS = {"PS", "PS2", "PS3", "PS4", "PS5", "PSP", "PSV"}

def extract_data(path: str, chunksize: int = 1000) -> pd.DataFrame:
    source = Path(path)
    if not source.exists():
        raise FileNotFoundError(f"No se encontró el archivo fuente: {source}")

    chunks = []
    for chunk in pd.read_csv(
        source,
        encoding="utf-8",
        delimiter=",",
        low_memory=False,
        chunksize=chunksize
    ):
        platform = chunk["Platform"].astype("string").str.strip().str.upper()
        chunk = chunk[platform.isin(PLAYSTATION_PLATFORMS)].copy()
        chunks.append(chunk)

    if not chunks:
        return pd.DataFrame()

    return pd.concat(chunks, ignore_index=True)

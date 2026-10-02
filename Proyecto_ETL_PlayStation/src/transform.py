import pandas as pd

NUMERIC_COLUMNS = [
    "Year_of_Release", "NA_Sales", "EU_Sales", "JP_Sales",
    "Other_Sales", "Global_Sales", "Critic_Score", "User_Score"
]

TEXT_COLUMNS = ["Name", "Platform", "Genre", "Publisher", "Rating"]

def profile_data(df: pd.DataFrame) -> dict:
    return {
        "filas": int(len(df)),
        "columnas": int(len(df.columns)),
        "completitud_porcentaje": round(float(df.notna().mean().mean() * 100), 2),
        "duplicados": int(df.duplicated().sum()),
        "nulos_por_columna": {k: int(v) for k, v in df.isna().sum().items()},
    }

def transform_data(df: pd.DataFrame):
    data = df.copy()
    before = len(data)

    for col in TEXT_COLUMNS:
        if col in data.columns:
            data[col] = data[col].astype("string").str.strip()

    data["Platform"] = data["Platform"].str.upper()
    data["Genre"] = data["Genre"].str.title()
    data["Publisher"] = data["Publisher"].replace("", pd.NA)
    data["Name"] = data["Name"].str.replace(r"\s+", " ", regex=True)

    for col in NUMERIC_COLUMNS:
        data[col] = pd.to_numeric(data[col], errors="coerce")

    # "tbd" en User_Score se convierte en NaN y se conserva como desconocido.
    data["Year_of_Release"] = data["Year_of_Release"].where(
        data["Year_of_Release"].between(1970, 2030)
    )

    data["Genre"] = data["Genre"].fillna("Unknown")
    data["Publisher"] = data["Publisher"].fillna("Unknown")
    data["Rating"] = data["Rating"].fillna("Unknown")

    # Unicidad del registro: juego + plataforma + año.
    data = data.drop_duplicates(
        subset=["Name", "Platform", "Year_of_Release"],
        keep="first"
    )

    data["Global_Sales"] = data["Global_Sales"].fillna(
        data[["NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales"]].sum(axis=1, min_count=1)
    )

    data = data.sort_values(["Year_of_Release", "Name"], na_position="last")
    data = data.reset_index(drop=True)

    profile_after = profile_data(data)
    profile_after["filas_antes"] = before
    profile_after["filas_despues"] = len(data)
    profile_after["duplicados_eliminados"] = before - len(data)

    return data, profile_after

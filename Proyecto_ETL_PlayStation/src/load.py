from pathlib import Path
import sqlite3
import pandas as pd

def load_to_sqlite(df: pd.DataFrame, db_path: str, table_name: str = "games") -> None:
    db = Path(db_path)
    db.parent.mkdir(parents=True, exist_ok=True)

    with sqlite3.connect(db) as conn:
        conn.execute(f"DROP TABLE IF EXISTS {table_name}")
        df.to_sql(table_name, conn, if_exists="replace", index=False)
        conn.execute(
            f"CREATE INDEX IF NOT EXISTS idx_{table_name}_platform "
            f"ON {table_name}(Platform)"
        )
        conn.execute(
            f"CREATE INDEX IF NOT EXISTS idx_{table_name}_year "
            f"ON {table_name}(Year_of_Release)"
        )
        conn.commit()

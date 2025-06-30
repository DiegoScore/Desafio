import pandas as pd
import logging

def cargar_datos(ruta: str, columna_texto: str = "texto") -> pd.DataFrame:
    logging.info(f"Cargando datos desde: {ruta}")
    df = pd.read_csv(ruta)
    df["fecha"] = pd.to_datetime(df["fecha"], errors="coerce")
    df = df[~df[columna_texto].isnull() & df[columna_texto].str.strip().ne("")]
    logging.info(f"{len(df)} documentos cargados.")
    return df
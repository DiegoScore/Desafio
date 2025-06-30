from bertopic import BERTopic
from app.config import RUTA_MODELO, RUTA_SALIDA
import pandas as pd
import logging

def exportar_resumen_topicos():
    logging.info("Exportando resumen de temas...")
    modelo = BERTopic.load(RUTA_MODELO)
    df_temas = modelo.get_topic_info()

    output_csv = f"{RUTA_SALIDA}/temas_resumen.csv"
    df_temas.to_csv(output_csv, index=False)

    output_excel = f"{RUTA_SALIDA}/temas_resumen.xlsx"
    df_temas.to_excel(output_excel, index=False)

    logging.info(f"Resumen exportado a:\n - CSV: {output_csv}\n - Excel: {output_excel}")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    exportar_resumen_topicos()
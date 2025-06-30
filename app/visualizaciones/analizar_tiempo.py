from bertopic import BERTopic
from app.config import RUTA_MODELO, RUTA_DATOS, RUTA_SALIDA, COLUMNA_TEXTO
from app.preprocesamiento import cargar_datos
import logging

def analizar_evolucion_temporal():
    logging.info("Cargando modelo y datos para análisis temporal...")
    df = cargar_datos(RUTA_DATOS, COLUMNA_TEXTO)
    modelo = BERTopic.load(RUTA_MODELO)

    logging.info("Calculando evolución de temas...")
    topics_over_time = modelo.topics_over_time(df[COLUMNA_TEXTO].tolist(), df["fecha"])
    fig = modelo.visualize_topics_over_time(topics_over_time)

    output_path = f"{RUTA_SALIDA}/temas_por_tiempo.html"
    fig.write_html(output_path)
    logging.info(f"Visualización temporal exportada a: {output_path}")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    analizar_evolucion_temporal()

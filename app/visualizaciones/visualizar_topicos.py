from bertopic import BERTopic
from app.config import RUTA_MODELO, RUTA_SALIDA
import logging

def visualizar_topicos():
    logging.info("Cargando modelo para visualización interactiva...")
    modelo = BERTopic.load(RUTA_MODELO)

    fig = modelo.visualize_topics()
    output_path = f"{RUTA_SALIDA}/temas_interactivos.html"
    fig.write_html(output_path)

    logging.info(f"Visualización exportada a: {output_path}")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    visualizar_topicos()
import logging
from config import RUTA_DATOS, RUTA_MODELO, COLUMNA_TEXTO
from preprocesamiento import cargar_datos
from modelo import inicializar_modelo, entrenar_y_guardar_modelo

logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    df = cargar_datos(RUTA_DATOS, COLUMNA_TEXTO)
    modelo = inicializar_modelo()
    entrenar_y_guardar_modelo(df[COLUMNA_TEXTO].tolist(), modelo, RUTA_MODELO)

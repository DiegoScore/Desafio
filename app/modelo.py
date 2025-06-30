from bertopic import BERTopic
from sentence_transformers import SentenceTransformer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction import text
from umap import UMAP
import hdbscan
import logging

def inicializar_modelo() -> BERTopic:
    logging.info("Inicializando modelo BERTopic...")

    embedding_model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")
    stopwords_es = text.ENGLISH_STOP_WORDS.union([
        "dijo", "años", "año", "mil", "ser", "estar", "tener", "haber",
        "así", "también", "puede", "cada", "nuevo", "tras", "entre",
        "luego", "aunque", "porque", "mientras", "cuando", "más",
        "pero", "uno", "dos", "tres", "además", "aún", "ya", "sin",
        "antes", "después", "sobre", "durante", "según", "hoy", "ayer",
        "en", "la", "de", "cve", "spa", "y", "lo", "su", "como", "que", "con",
        "por", "los", "las", "e", "o", "es", "para", "el", "se", "todo", "desde",
        "una", "un", "este", "eso", "esto", "esta", "al", "del", "se", "fue", "solo",
        "sino", "son", "ha", "sea", "ella", "cual", "sus", "nos","muy","donde", "hay",
        "está","horas","parte"
    ])
    umap_model = UMAP(n_neighbors=15, n_components=5, min_dist=0.0, metric='cosine')
    hdbscan_model = hdbscan.HDBSCAN(min_cluster_size=10, metric='euclidean', prediction_data=True)
    vectorizer_model = CountVectorizer(stop_words=list(stopwords_es))

    modelo = BERTopic(
        embedding_model=embedding_model,
        umap_model=umap_model,
        hdbscan_model=hdbscan_model,
        vectorizer_model=vectorizer_model,
        calculate_probabilities=True,
        verbose=True
    )
    return modelo

def entrenar_y_guardar_modelo(textos: list[str], modelo: BERTopic, ruta: str):
    logging.info("Entrenando modelo BERTopic...")
    modelo.fit(textos)
    modelo.save(ruta)
    logging.info(f"✅ Modelo guardado en: {ruta}")

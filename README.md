# Plan de Acción: Análisis de Noticias con BERTopic
## Uso de BERTopic

Al analizar un corpus de 6399 noticias de diversas fuentes chilenas, se optó por utilizar **BERTopic**, una biblioteca de Open Source que aprovecha BERT (Un algoritmo de Google capaz de captar el contexto de una oración) y TF-IDF(Que es la frecuencia en la que aparece un término y su frecuencia inversa en un documento). Esta técnica de modelado se basa en clases para crear grupos densos que permiten agrupar temas fácilmente interpretables, mientras que se mantienen las palabras importantes en la descripción de los temas.
### ¿Por qué BERTopic?
- **Modelo No Supervisado**: No requiere etiquetas previas y es ideal este tipo de modelos para este desafío.
- **Embeddings semánticos**: Utilizando modelos preentrenados como `SentenceTransformer` podemos reducir la memoria al vectorizar palabras y reducir su dimensionalidad aumentando la eficiencia del modelo y simplificando el procesamiento y almacenamiento de los datos, pero manteniendo las relaciones semánticas y contexto del texto.
- **Reducción de Dimensionalidad**: Utilizando UMAP se reduce la dimensionalidad bajando aún más la dimensión de los datos.
- **Clustering Robusto**: Utilizando HDBSCAN que es un algoritmo de agrupación basado en densidad, se pueden generar clusters más robustos detectando agrupamientos naturales, permitiendo descubrir tópicos más frecuentes.
---
## Plan de Acción
1. ### Construcción del Contenedor
   - Se configuró una imagen de Docker  `nvidia/cuda:12.2.0-runtime-ubuntu20.04`, esta específicamente por las capacidades de mi PC. Junto con su respectivo `DockerFile` y `docker-compose.yml`.
   - Se instalaron las dependencias necesarias: `Python 3.10`, `PyTorch con CUDA`, `BERTopic`, principalmente. Todos descritos en `requirements.txt`.
   - Esta construcción se montó en un volumen el proyecto completo (`/Desafio`) y se configuró `PyCharm` como IDE host.
2. ### Exploración y Limpieza del Dataset
    - Se identificaron y eliminaron **661 duplicados**.
    - Se combinó los datos de: `titulo`, `bajada` y `cuerpo` en una nueva columna `texto`.
    - Se analizaron fechas, largo de texto y campos faltantes.
    - Se graficaron sus estadísticas descriptivas y gráficas de la distribución temporal.
3. ### Preprocesamiento de datos
   - Se limpió el dataset, eliminando los 661 duplicados, con lo que nos dejó un total de  **5738 noticias** para utilizar, guardadas en  `/data/noticias_limpias.csv`.
   - Luego pasa por un preprocesamiento en donde se carga el archivo `noticias_limpias.csv` y se revisan errores de fechas mal formateadas y las transforma a NaT, luego filtra el DataFrame eliminando las filas en donde `texto` esté `NaN`.
4. ### Entrenamiento Modelo
   - Se inicializa un pipeline:
    - `SentenceTransformer`: `paraphrase-multilingual-MiniLM-L12-v2`
     - `UMAP`: `n_neighbors=15, n_components=5, min_dist=0.0`
     - `HDBSCAN`: `min_cluster_size=10` Por recomendación y generalidad se utilizan 10 clusters como mínimo con este tamaño de corpus.
     - `CountVectorizer`: utilizando lista personalizada de stopwords vistas en el mapa de palabras.
     - Se entrenó el modelo en GPU con 5738 noticias procesadas.
5. ### Resultados Guardados
   - El notebook `WordClouds.ipynb` generó nubes de palabras correspondientes a cada sección y cada medio, guardados en `/output/wordsclouds`.
   - Se exportó el modelo entrenado a  `output/bertopic_model`.
   - Se generó un  `.csv` y `.xlsx` con el resumen de los tópicos.
   - Se guardó una visualización con `plotly` como `HTML` y también una visualización de la evolución de los tópicos en una línea de tiempo.
---
# Instrucciones de ejecución
   - (OPCIONAL) Contar con docker, sino instalar `requirements.txt`, `pip install -r requirements.txt`.
   - Al descargar este proyecto, no hace falta ejecutar `eda.ipynb` ya que este nos entrega el csv `noticias_limpias.csv`. **En caso de requerir la limpieza de noticias ejecutar todas las celdas**.
   - Ejecutar `main.py` para entrenar el modelo y guardarlo.
   - Ejecutar visualizaciones: `analizar_tiempo.py`(Visualización temporal), `resumen_topicos.py`(Archivo `.csv` y `.xlxs` con los temas agrupados) y `visualizar_topicos.py`(Visualización `plotly`).
---
# Conclusión
Como desafío fue muy entretenido realizarlo, lo común en esta área es encontrarse con desafíos de modelos supervisados, por lo que me sorprendió para bien esta oportunidad.
No había realizado este tipo de problemas y la verdad me sorprendieron los resultados, mi primer enfoque iba directamente al clustering con Kmeans, pero no satisfacía la necesidad de contexto y coherencia que requería el desafío por lo que encontrarme con la solución implementando BERT fue interesante y pude aprender bastante de su funcionamiento más moderno y enfocado en la semántica.
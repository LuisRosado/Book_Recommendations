import pandas as pd
import csv
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Cargar y limpiar el dataset
df = pd.read_csv('data/books.csv', 
                 quoting=csv.QUOTE_MINIMAL,
                 escapechar='\\',
                 on_bad_lines='skip')

# Renombrar la columna problemática
df = df.rename(columns={' num_pages': 'num_pages'})

df = df.dropna()  # Eliminar filas con valores nulos
df['title'] = df['title'].str.lower()  # Estandarizar títulos

# Asegúrate de que todas las columnas necesarias existen
required_columns = ['title', 'authors', 'average_rating']
for col in required_columns:
    if col not in df.columns:
        raise ValueError(f"La columna '{col}' no está presente en el CSV")

# Crear una columna de características combinando título, autor y calificación promedio
df['features'] = df['title'] + ' ' + df['authors'] + ' ' + df['average_rating'].astype(str)

# Crear la matriz TF-IDF
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(df['features'])

def get_recommendations(title, top_n=5):
    title = title.lower()
    if title not in df['title'].values:
        return []
    
    idx = df[df['title'] == title].index[0]
    sim_scores = list(enumerate(cosine_similarity(tfidf_matrix[idx], tfidf_matrix)[0]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:top_n+1]
    book_indices = [i[0] for i in sim_scores]
    
    recommended_books = df.iloc[book_indices][['title', 'authors', 'average_rating']]
    return recommended_books.to_dict('records')

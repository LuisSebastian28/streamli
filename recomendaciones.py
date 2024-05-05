import pandas as pd
from sklearn.preprocessing import MinMaxScaler

ruta_csv = "google_review_ratings.csv"
dataframe = pd.read_csv(ruta_csv)
category_ratings = st.session_state.get("category_ratings", None)


# Definir un diccionario para mapear los nombres de las columnas
nuevos_nombres = {
    'Category 1': 'iglesias',
    'Category 2': 'resorts',
    'Category 3': 'playas',
    'Category 4': 'parques',
    'Category 5': 'teatros',
    'Category 6': 'museos',
    'Category 7': 'centros comerciales',
    'Category 8': 'zoológicos',
    'Category 9': 'restaurantes',
    'Category 10': 'pubs/bares',
    'Category 11': 'servicios locales',
    'Category 12': 'hamburgueserías/pizzerías',
    'Category 13': 'hoteles/otros alojamientos',
    'Category 14': 'bares de jugos',
    'Category 15': 'galerías de arte',
    'Category 16': 'clubes de baile',
    'Category 17': 'piscinas',
    'Category 18': 'gimnasios',
    'Category 19': 'panaderías',
    'Category 20': 'belleza y spas',
    'Category 21': 'cafeterías',
    'Category 22': 'miradores',
    'Category 23': 'monumentos',
    'Category 24': 'jardines'
}
dataframe = dataframe.rename(columns=nuevos_nombres)

tipos_de_dato = dataframe.dtypes

# Eliminar las columnas especificadas
columns_to_drop = ['playas', 'clubes de baile', 'gimnasios', 'panaderías', 'Unnamed: 25']
dataframe_cleaned = dataframe.drop(columns=columns_to_drop)

tipos_de_dato = dataframe.dtypes

# Seleccionar únicamente la fila de "servicios locales"
fila_servicios_locales = dataframe_cleaned.loc[:, 'servicios locales']

# Filtrar la fila "servicios locales" y seleccionar solo los datos de tipo object
fila_servicios_locales_object = dataframe_cleaned.loc[:, 'servicios locales'][dataframe_cleaned.loc[:, 'servicios locales'].apply(lambda x: isinstance(x, object))]

# Obtener el tamaño del DataFrame
filas, columnas = dataframe_cleaned.shape

# Eliminar la columna 'servicios locales'
dataframe_cleaned = dataframe_cleaned.drop('servicios locales', axis=1)
dataframe_cleaned = dataframe_cleaned.drop('User', axis=1)

tipos_de_dato = dataframe_cleaned.dtypes

# Seleccionar solo las columnas numéricas para redondear
columns_to_round = dataframe_cleaned.select_dtypes(include=['float64']).columns

# Redondear las columnas seleccionadas individualmente
for column in columns_to_round:
    dataframe_cleaned[column] = dataframe_cleaned[column].round()

tipos_de_dato = dataframe_cleaned.dtypes


import numpy as np

# Reemplazar valores no finitos con 0 en el DataFrame
dataframe_cleaned.replace([np.inf, -np.inf, np.nan], 0, inplace=True)

# Redondear todas las columnas flotantes a enteros
dataframe_rounded = dataframe_cleaned.round().astype(int)

tipos_de_dato = dataframe_rounded.dtypes

# Encontrar valores nulos en el DataFrame
valores_nulos = dataframe_rounded.isnull().sum()

import numpy as np

# Generar calificaciones aleatorias del 1 al 5 para los lugares de interés
calificaciones = category_ratings

from sklearn.metrics.pairwise import cosine_similarity

# Normalizar los datos si es necesario
scaler = MinMaxScaler()
data_normalized = scaler.fit_transform(dataframe_rounded)

# Calcular la matriz de similitud coseno
similarity_matrix = cosine_similarity(data_normalized, data_normalized)

# Obtener el índice del usuario que deseas comparar
user_index = 0  # Cambia esto según el usuario que quieras comparar

# Obtener las similitudes del usuario con todos los demás usuarios
user_similarities = similarity_matrix[user_index]

# Mostrar las similitudes del usuario con todos los demás usuarios
for idx, similarity in enumerate(user_similarities):
    if idx != user_index:  # Evitar comparar con el mismo usuario
        print(f"Usuario #{idx}: Similitud = {similarity}")
sorted_indices = []
most_similar_user_index = sorted_indices[1]  # El primer índice es el propio usuario, así que tomamos el segundo más cercano

# Obtener las calificaciones del usuario similar más cercano
most_similar_user_ratings = dataframe_rounded.iloc[most_similar_user_index]

# Mostrar las calificaciones del usuario similar más cercano
for category, rating in most_similar_user_ratings.items():
    print(f"- {category}: {rating}")

# Obtener las calificaciones del usuario similar más cercano
most_similar_user_ratings = dataframe_rounded.iloc[most_similar_user_index]

# Ordenar las calificaciones de mayor a menor
sorted_ratings = most_similar_user_ratings.sort_values(ascending=False)

# Obtener la lista de categorías ordenadas
sorted_categories = sorted_ratings.index.tolist()

print("Lista de categorías ordenadas según las calificaciones del usuario similar más cercano:")
print(sorted_categories)

from googletrans import Translator

# Función para traducir una lista de categorías al inglés
def translate_categories(categories):
    translator = Translator()
    translated_categories = []
    for category in categories:
        translated = translator.translate(category, src='es', dest='en')
        translated_categories.append(translated.text)
    return translated_categories

# Obtener las calificaciones del usuario similar más cercano
most_similar_user_ratings = dataframe_rounded.iloc[most_similar_user_index]

# Ordenar las calificaciones de mayor a menor
sorted_ratings = most_similar_user_ratings.sort_values(ascending=False)

# Obtener la lista de categorías ordenadas
sorted_categories = sorted_ratings.index.tolist()

# Traducir la lista de categorías al inglés
sorted_categories_en = translate_categories(sorted_categories)

print("Lista de categorías ordenadas en inglés según las calificaciones del usuario similar más cercano:")
print(sorted_categories_en)

# Función para traducir una lista de categorías al inglés y concatenar con 'in Cochabamba'
def categories_concat(categories):
    concat_categories = []
    for category in categories:
        concat_categories.append(category + " in Bolivia")
    return concat_categories

# Traducir las categorías al inglés y concatenar con 'in Cochabamba'
concatenadas = categories_concat(sorted_categories_en)

import requests

# Definir la URL del endpoint de búsqueda de imágenes en Pexels
url = "https://api.pexels.com/v1/search"

# Definir el número de resultados por página
per_page = 5  # Obtendremos al menos 5 imágenes relacionadas por cada categoría

# Definir los encabezados con la llave de autorización
headers = {
    "Authorization": "wRPPpDBr6VdXCCn5HHihbgztCFG1p22s1UMezGpJn2ck5ndjtZC2GRc3"
}

# Realizar la solicitud GET a la API de Pexels para cada categoría concatenada
for category in concatenadas:
    # Realizar la solicitud GET para la categoría actual
    response = requests.get(url, params={"query": category, "per_page": per_page}, headers=headers)
    
    # Verificar si la solicitud fue exitosa (código de respuesta 200)
    if response.status_code == 200:
        # Obtener los resultados de la respuesta JSON
        data = response.json()
        # Procesar los resultados para mostrar las imágenes de la categoría actual
        if data["total_results"] > 0:
            print(f"Imágenes relacionadas con {category}:")
            for result in data["photos"]:
                print(f"Imagen: {result['url']}")
        else:
            print(f"No se encontraron imágenes relacionadas con {category}.")
    else:
        print(f"Error al realizar la solicitud a la API de Pexels para la categoría {category}.")

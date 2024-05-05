import streamlit as st
import requests

def obtener_imagenes_desde_api(query, api_key):
    url_api = "https://api.pexels.com/v1/search"
    headers = {
        "Authorization": api_key
    }
    params = {
        "query": query
    }

    try:
        response = requests.get(url_api, headers=headers, params=params)
        if response.status_code == 200:
            data = response.json()
            return data.get("photos", [])
        else:
            st.error(f"Error al obtener imágenes de la API: {response.status_code}")
            return []
    except Exception as e:
        st.error(f"Error al conectarse a la API: {e}")
        return []

def inicio():
    api_key = "wRPPpDBr6VdXCCn5HHihbgztCFG1p22s1UMezGpJn2ck5ndjtZC2GRc3"
    st.title("Inicio")
    st.header("¡Lo Más Recomendado!")
    st.write("Aquí encontrarás algunas de nuestras recomendaciones principales.")

    query = "tourism Bolivia"
    imagenes = obtener_imagenes_desde_api(query, api_key)

    if imagenes:
        num_columnas = 4
        num_imagenes = len(imagenes)
        num_filas = (num_imagenes + num_columnas - 1) // num_columnas
        for fila in range(num_filas):
            cols = st.columns(num_columnas)
            for i in range(num_columnas):
                index = fila * num_columnas + i
                if index < num_imagenes:
                    imagen_url = imagenes[index].get("src", {}).get("large", "")
                    cols[i].image(imagen_url, width=200, caption=f"Imagen {index+1}", use_column_width=True)
    else:
        st.warning("No se encontraron imágenes disponibles en la API.")

    st.header("Mis Lugares a Visitar")
    st.write("Estos son algunos de los lugares que me gustaría visitar en el futuro:")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.image("https://via.placeholder.com/200", caption="Lugar 1")
    with col2:
        st.image("https://via.placeholder.com/200", caption="Lugar 2")
    with col3:
        st.image("https://via.placeholder.com/200", caption="Lugar 3")
    with col4:
        st.image("https://via.placeholder.com/200", caption="Lugar 4")

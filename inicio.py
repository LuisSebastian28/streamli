import streamlit as st
import requests
import re
import google.generativeai as ggi


def generar_lucares_recomendados(destino):
    lugares = []
    user_quest = "Dame cinco lugares para visitar en " + destino + " Bolivia"
    response_words = []

    api_key_gemini="AIzaSyAzFvpz7EfB1RJIN9zT_QwWPMu-pkPYrlI"

    ggi.configure(api_key=api_key_gemini)

    model = ggi.GenerativeModel("gemini-pro")
    chat = model.start_chat()

    def LLM_Response(question):
        response = chat.send_message(question, stream=True)
        return response


    result = LLM_Response(user_quest)
    for word in result:
        response_words.append(word.text)
    for linea in response_words:
        lugar_match = re.search(r'\*(.+?):', linea)
        if lugar_match:
            lugares.append(lugar_match.group(1).strip())
    return lugares

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

    destino = st.selectbox('Elige una opción', ('cochabamba', 'oruro', 'la paz'), index=0)

    st.header("¡Lo Más Recomendado!")
    st.write("Aquí encontrarás algunas de nuestras recomendaciones principales.")

    lugares = generar_lucares_recomendados(destino)

    for lugar in lugares:
        query = lugar + "de Bolivia"
        imagenes = obtener_imagenes_desde_api(query, api_key)

        if imagenes:
            imagen_url = imagenes[0].get("src", {}).get("large", "")
            st.image(imagen_url, width=200, caption=lugar, use_column_width=True)
        else:
            st.warning(f"No se encontraron imágenes disponibles para {lugar}.")

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

    

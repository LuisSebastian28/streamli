import streamlit as st
import requests
import re
import google.generativeai as ggi
from bs4 import BeautifulSoup
import urllib.parse

def generar_busqueda_recomendados(destino, busqueda):
    lugares = []
    user_quest = "Dame diez " + busqueda + " para visitar en " + destino + " Bolivia"
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

def obtener_url_imagen_google(query):
    query_encoded = urllib.parse.quote(query)
    url = f"https://www.google.com/search?tbm=isch&q={query_encoded}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    img_tags = soup.find_all("img")
    img_urls = [img["src"] for img in img_tags]
    return img_urls[1]

def inicio():
    st.title("Inicio")

    destino = st.selectbox('Elige una opción', ('cochabamba', 'oruro', 'la paz'), index=0)

    st.header("¡Los Lugares Más Recomendado!")
    st.write("Aquí encontrarás algunas de nuestras recomendaciones principales.")

    lugares = generar_busqueda_recomendados(destino, "lugares")

    for lugar in lugares:
        query = lugar + " Bolivia"
        imagen_url = obtener_url_imagen_google(query)
        if imagen_url:
            st.image(imagen_url, caption=lugar, use_column_width=True)
        else:
            st.write("No se encontró una imagen para esta comida en Google.")

    st.header("¡Las Comidas Más Recomendadas!")
    st.write("Aquí encontrarás algunas de nuestras recomendaciones principales.")

    comidas = generar_busqueda_recomendados(destino, "comidas")

    for comida in comidas:
        query = comida + " Bolivia"
        imagen_url = obtener_url_imagen_google(query)
        if imagen_url:
            st.image(imagen_url, caption=comida, use_column_width=True)
        else:
            st.write("No se encontró una imagen para esta comida en Google.")

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

    

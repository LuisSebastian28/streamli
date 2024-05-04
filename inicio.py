import streamlit as st

def inicio():
    st.title("Inicio")
    st.header("¡Lo Más Recomendado!")
    st.write("Aquí encontrarás algunas de nuestras recomendaciones principales.")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.image("https://via.placeholder.com/200", caption="Imagen 1")
    with col2:
        st.image("https://via.placeholder.com/200", caption="Imagen 2")
    with col3:
        st.image("https://via.placeholder.com/200", caption="Imagen 3")
    with col4:
        st.image("https://via.placeholder.com/200", caption="Imagen 4")
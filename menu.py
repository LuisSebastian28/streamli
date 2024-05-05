import streamlit as st
from streamlit_option_menu import option_menu
from inicio import inicio
from mi_perfil import mi_perfil

def menu():
    with st.sidebar:
        selected = option_menu("Menu", ["Inicio", "Chatbot", "Mi perfil"], icons=["house", "chat", "person"], menu_icon="cast", default_index=0)

    if selected == "Inicio":
        inicio()
    if selected == "Mi perfil":
        mi_perfil()
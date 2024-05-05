import streamlit as st
from streamlit_option_menu import option_menu
from inicio import inicio
from mi_perfil import mi_perfil
from chatbot import chatbot
from inicio_sesion import inicio_sesion

def on_click_registrarse():
    st.session_state["page"] = "inicio de sesion"

def menu():
    with st.sidebar:
        selected = option_menu("Menu", ["Inicio", "Chatbot", "Mi perfil", "Cerrar sesion"], icons=["house", "chat", "person", "door-open"], menu_icon="bars", default_index=0)

    if selected == "Inicio":
        inicio()
    if selected == "Chatbot":
        chatbot()
    if selected == "Mi perfil":
        mi_perfil()
    if selected == "Cerrar sesion":
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.experimental_rerun()
        
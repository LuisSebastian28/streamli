import streamlit as st
from menu import menu
from account import preguntas_usuario
from inicio_sesion import inicio_sesion

if "page" not in st.session_state:
    st.session_state["page"] = "inicio de sesion"

if st.session_state["page"] == "inicio de sesion":
    inicio_sesion()
if st.session_state["page"] == "account":
    preguntas_usuario()
if st.session_state["page"] == "menu":
    menu()

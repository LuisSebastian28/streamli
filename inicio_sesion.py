import streamlit as st

def inicio_sesion():
    st.title("Inicio de sesión")

    email = st.text_input("Correo electrónico:")
    password = st.text_input("Contraseña:", type="password")

    def on_click_registro():
        st.session_state["page"] = "account"

    def on_click_inicio():
        if email and password:
            st.session_state["page"] = "menu"
        else:
            st.warning("Por favor, ingrese su correo electrónico y contraseña.")


    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.write("")
    with col2:
        st.button("Iniciar sesión", on_click=on_click_inicio)
    with col3:
        st.button("Registrarse", on_click=on_click_registro)
    with col4:
        st.write("")
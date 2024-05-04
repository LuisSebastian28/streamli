import streamlit as st

def inicio():
    st.title('Saludo')
    st.write('Hola')

def registro():
    st.title("Inicio de sesión")

    email = st.text_input("Correo electrónico:")
    password = st.text_input("Contraseña:", type="password")

    def on_click():
        if email and password:
            st.session_state['page'] = 'inicio'
        else:
            st.warning("Por favor, ingrese su correo electrónico y contraseña.")

    st.button("Iniciar sesión", on_click=on_click)

if 'page' not in st.session_state:
    st.session_state['page'] = 'registro'

if st.session_state['page'] == 'registro':
    registro()
elif st.session_state['page'] == 'inicio':
    inicio()

import streamlit as st
import time

def simulate_loading(email, password):
    with st.spinner("Autenticando..."):
        time.sleep(5)
        st.success("¡Autenticación exitosa!")

        
def inicio():
    st.title('Saludo')
    st.write('Hola')

def registro():
    st.title("Página de Carga en Streamlit")

    email = st.text_input("Correo electrónico:")
    password = st.text_input("Contraseña:", type="password")

    if st.button("Iniciar carga"):
        if email and password:
            simulate_loading(email, password)
            st.session_state['page'] = 'inicio'
        else:
            st.warning("Por favor, ingrese su correo electrónico y contraseña.")

if 'page' not in st.session_state:
    st.session_state['page'] = 'registro'

if st.session_state['page'] == 'registro':
    registro()
elif st.session_state['page'] == 'inicio':
    inicio()
import streamlit as st
import time

def simulate_loading(email, password):
    with st.spinner("Autenticando..."):
        time.sleep(5)
        st.success("¡Autenticación exitosa!")

def main():
    st.title("Inicio")

    email = st.text_input("Correo electrónico:")
    password = st.text_input("Contraseña:", type="password")

    if st.button("Iniciar session"):
        if email and password:
            simulate_loading(email, password)
        else:
            st.warning("Por favor, ingrese su correo electrónico y contraseña.")

if __name__ == "__main__":
    main()

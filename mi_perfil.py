import streamlit as st

def mi_perfil():
    st.title("Mi Perfil")

    nombre = st.text_input("Nombre", "John Doe")
    edad = st.number_input("Edad", min_value=0, max_value=150, value=30)
    email = st.text_input("Correo Electrónico", "john.doe@example.com")
    telefono = st.text_input("Teléfono", "+1234567890")

    st.write("## Información del Usuario")
    st.write(f"**Nombre:** {nombre}")
    st.write(f"**Edad:** {edad}")
    st.write(f"**Correo Electrónico:** {email}")
    st.write(f"**Teléfono:** {telefono}")
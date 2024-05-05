import streamlit as st
import google.generativeai as ggi


def on_click_registrarse():
    st.session_state["page"] = "menu"


def preguntas_usuario():
    st.title("¡Bienvenido a nuestra guía de turismo!")
    st.write(
        "Por favor, califica tu interés en las siguientes categorías (del 1 al 5):"
    )

    categories = {
        "Category 1": "Iglesias",
        "Category 2": "Resorts",
        "Category 4": "Parques",
        "Category 5": "Teatros",
        "Category 6": "Museos",
        "Category 7": "Centros comerciales",
        "Category 8": "Zoológicos",
        "Category 9": "Restaurantes",
        "Category 10": "Pubs/Bares",
        "Category 12": "Hamburgueserías/Pizzerías",
        "Category 13": "Hoteles/Otros alojamientos",
        "Category 14": "Bares de jugos",
        "Category 15": "Galerías de arte",
        "Category 17": "Piscinas",
        "Category 20": "Belleza y spas",
        "Category 21": "Cafeterías",
        "Category 22": "Miradores",
        "Category 23": "Monumentos",
        "Category 24": "Jardines",
    }

    category_ratings = {}
    for category, label in categories.items():
        category_ratings[category] = st.slider(label, 1, 5)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.write("")
    with col2:
        st.button(
            "Registrarse", on_click=on_click_registrarse
        )  # Remove parentheses here
    with col3:
        st.write("")
    # Return the category_ratings dictionary
    st.session_state["category_ratings"] = category_ratings


preguntas_usuario()

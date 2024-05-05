import streamlit as st
import google.generativeai as ggi
from PyPDF2 import PdfReader

def leer_pdf(pdf_file):
    text = ""
    with open(pdf_file, "rb") as file:
        pdf_reader = PdfReader(file)
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
    return text


def chatbot():

    fetcheed_api_key = "AIzaSyAzFvpz7EfB1RJIN9zT_QwWPMu-pkPYrlI"
    ggi.configure(api_key = fetcheed_api_key)

    model = ggi.GenerativeModel("gemini-pro") 
    chat = model.start_chat()

    
    def LLM_Response(question):
        response = chat.send_message(question,stream=True)
        return response

    st.title("Chatbot")
    pdf_file = "recopilacion 2 demo.pdf"
    pdf_text = leer_pdf(pdf_file)

    user_quest = st.text_input("Pregunta:")
    btn = st.button("Preguntar")

    if btn and user_quest:
        result = LLM_Response(user_quest + "\n" + pdf_text)
        st.subheader("Respuesta : ")
        for word in result:
            st.text(word.text)
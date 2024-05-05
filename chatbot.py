import streamlit as st
import google.generativeai as ggi


def chatbot():

    fetcheed_api_key = "AIzaSyAzFvpz7EfB1RJIN9zT_QwWPMu-pkPYrlI"
    ggi.configure(api_key = fetcheed_api_key)

    model = ggi.GenerativeModel("gemini-pro") 
    chat = model.start_chat()

    
    def LLM_Response(question):
        response = chat.send_message(question,stream=True)
        return response

    st.title("Chatbot")

    user_quest = st.text_input("Pregunta:")
    btn = st.button("Preguntar")

    if btn and user_quest:
        result = LLM_Response(user_quest)
        st.subheader("Response : ")
        for word in result:
            st.text(word.text)
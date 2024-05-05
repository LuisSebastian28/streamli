import streamlit as st

def preguntas_usuario():
    st.title("¡Bienvenido a nuestra guía de turismo!")
    st.write("Por favor, responde algunas preguntas para recomendarte lugares turísticos en nuestra ciudad:")

    actividades_interes = st.selectbox("¿Qué tipo de actividades te interesan más durante tus viajes?",
                                      ["Aventura y deportes extremos", "Arte y cultura", "Naturaleza y ecoturismo",
                                       "Gastronomía y vinos", "Relax y bienestar", "Historia y patrimonio"])

    tipo_lugares = st.selectbox("¿Prefieres lugares históricos, naturales o culturales?",
                                ["Históricos", "Naturales", "Culturales"])

    tiempo_estadia = st.selectbox("¿Cuánto tiempo planeas estar en la ciudad?",
                                  ["Menos de 3 días", "De 3 a 5 días", "De 1 semana a 10 días", "Más de 10 días"])

    ubicacion_preferida = st.selectbox("¿Tienes alguna preferencia en cuanto a la ubicación de los lugares?",
                                       ["En el centro de la ciudad", "Cerca de transporte público",
                                        "En las afueras, en contacto con la naturaleza"])

    gastronomia_local = st.radio("¿Te interesa la gastronomía local y probar platos típicos?",
                                 ["Sí, me encanta probar la comida local", "Prefiero opciones internacionales y gourmet",
                                  "No tengo preferencia en este aspecto"])

    viaje_grupo = st.radio("¿Viajas con niños o en grupo?",
                           ["Con niños", "En grupo", "Actividades orientadas a adultos"])

    explorar_tours = st.radio("¿Te gusta explorar por tu cuenta o prefieres tours guiados?",
                              ["Explorar por mi cuenta", "Tours guiados", "Una combinación de ambos"])

    transporte_preferido = st.selectbox("¿Hay algún tipo de transporte que prefieras usar?",
                                        ["Transporte público", "Bicicleta o caminatas", "Autos de alquiler o taxis"])

    accesibilidad_lugares = st.selectbox("¿Tienes alguna restricción o preferencia en cuanto a la accesibilidad de los lugares?",
                                         ["Accesibles para personas con movilidad reducida",
                                          "Fácil acceso y poco desnivel", "No tengo restricciones en cuanto a accesibilidad"])

    combinar_actividades = st.radio("¿Te gustaría combinar actividades al aire libre con visitas a museos o sitios históricos?",
                                    ["Sí, me gusta tener una variedad de actividades",
                                     "Prefiero centrarme en un tipo de actividad",
                                     "No tengo preferencia, me adapto a las opciones disponibles"])

    st.write("Has seleccionado las siguientes preferencias:")
    st.write("- *Actividades de interés:*", actividades_interes)
    st.write("- *Tipo de lugares preferidos:*", tipo_lugares)
    st.write("- *Tiempo de estadía:*", tiempo_estadia)
    st.write("- *Ubicación preferida de los lugares:*", ubicacion_preferida)
    st.write("- *Preferencia gastronómica:*", gastronomia_local)
    st.write("- *Tipo de viaje:*", viaje_grupo)
    st.write("- *Preferencia de exploración:*", explorar_tours)
    st.write("- *Transporte preferido:*", transporte_preferido)
    st.write("- *Accesibilidad de los lugares:*", accesibilidad_lugares)
    st.write("- *Preferencia de actividades:*", combinar_actividades)

# Aquí podrías agregar la lógica para recomendar lugares basándote en las respuestas del usuario
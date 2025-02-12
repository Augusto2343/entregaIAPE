import streamlit as st
import openai
import dotenv
import os

openai.api_key=os.getenv('API_KEY')
lista=""
formato=""

def consejo (respuesta):
    st.text("HOLAAAA")
    if(respuesta == "si" or respuesta == "s" or respuesta=="Si" or respuesta=="SI"):
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content":f"Dale consejos al usuario de como reciclar los residuos de esta lista{lista}"
                }

    ])
        st.text(response.choices[0].message["content"])
    else:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content":"Dile adios al usuario."
                }

    ])
        st.text(response.choices[0].message["content"])
    btnContinuar=st.button("continuar")
    if btnContinuar:
        return inicio()
def devolverListaOrd(lista,formato):
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content":"Imagina que eres un separador de residuos y que te pasan la lista de residuos o un excel y vos el resultado en el formato que pida el usuario pero filtrada en residuo reciclable que tiene subdivisiones de carton,vidrio,papel y plástico, el residuo orgánico reciclable cascaras de verduras, frutas, semillas, etc y los residuos no reciclables que son curitas, papeles del baño y pañuelos. Sin introduccion ni nada y no respondas hasta que te pasen la lista.Al final de tu respuesta pregunta si quieren que les des consejos de como aprovechar los residuos reciclables solamente si los residuos que te paso son reciclables."
            },
            {
                "role": "user",
                "content":f"La lista es {lista}. Devolvemelo en el formato {formato}"
            }
            ]
)
    st.text(response.choices[0].message["content"])
    with st.form("Respuesta"):
        respuesta=st.text_input("Responda si o no")
        btnRes=st.form_submit_button("Responder")
    if btnRes:
        return consejo(respuesta)
    

def inicio():
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role":"user",
                "content":"Saluda al cliente."
            }
    ])
    st.text(response.choices[0].message["content"])
    with st.form("ingreso_residuos"):
        prompt=st.text_input("Ingrese su lista de residuos para organizarlos(separado por coma): ")
        formato=st.text_input("\nIngrese el formato (lista o json): ")
        submit=st.form_submit_button("procesar")
    if submit:
        lista= prompt.split(",")
        return devolverListaOrd(lista,formato)
    

st.title("Asistente de reciclaje.")
st.text("Este asistente utiliza IA de ChatGPT4o-mini para ordenar los productos en diferentes categorias y subcategorias Reciclable (metal, plastico, papel, organico) y no reciclable.")
inicio()
st.title("Como funciona")

st.text("Este asistente filtrador de residuos funciona en conjunto con la IA de OpenAI, python  y Streamlit.\n Los dos inputs del principio reciben los parametros como la lista de residuos y el formato de entrega de la lista ordenada por medio de funciones y con la integración de ChatGPT 4o-mini, ajustando su respuesta por medio de distintos prompts.\n Lo que da como resultado que te devuelva por pantalla los residuos ordenados en el formato que le hayas pedido.")
import openai
import dotenv
import os

openai.api_key=os.getenv('API_KEY')
lista=""
formato=""

def obtenerListRes():
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role":"user",
                "content":"Saluda al cliente."
            }
        ])
    print(response.choices[0].message["content"])
    prompt=input("Ingrese su lista de residuos para organizarlos(separado por coma): ")
    lista= prompt.split(",")
    print(lista)
    formato=input("\nIngrese el formato (lista o json): ")
    return devolverListaOrd(lista,formato)


def devolverListaOrd(lista,formato):
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content":"Imagina que eres un separador de residuos y que te pasan la lista de residuos o un excel y vos el resultado en el formato que pida el usuario pero filtrada en residuo reciclable que tiene subdivisiones de carton,vidrio,papel y plástico, el residuo orgánico reciclable cascaras de verduras, frutas, semillas, etc y los residuos no reciclables que son curitas, papeles del baño y pañuelos. Sin introduccion ni nada y no respondas hasta que te pasen la lista.Al final de tu respuesta pregunta si quieren que les des consejos de como aprovechar los residuos reciclables."
            },
            {
                "role": "user",
                "content":f"La lista es {lista}. Devolvemelo en el formato {formato}"
            }
            ]
)
    print(response.choices[0].message["content"])
obtenerListRes()
import json
import random

# Función para cargar las preguntas desde un archivo JSON
def cargar_preguntas(archivo):
    with open(archivo, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

# Cargar el archivo JSON con las preguntas
banco_preguntas = cargar_preguntas('questions.json')

def get_random_pregunta():
    banco_preguntas_list = list(banco_preguntas.keys())
    banco = random.choice(banco_preguntas_list)
    preguntas = banco_preguntas[banco]
    pregunta = random.choice(preguntas)
    return pregunta
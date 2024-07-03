import random
import pygame
from animaciones import *

posicion_1 = (150, 500)
posicion_2 = (250, 500)
posicion_3 = (350, 500)
posicion_4 = (450, 500)
posicion_5 = (575, 500)
posiciones = [posicion_1, posicion_2, posicion_3, posicion_4, posicion_5]

votantes = [
    {"nombre": "votante 1", "decision": None},
    {"nombre": "votante 2", "decision": None},
    {"nombre": "votante 3", "decision": None},
    {"nombre": "votante 4", "decision": None},
    {"nombre": "votante 5", "decision": None},
]

def generar_votos_con_posiciones():
    votos = [random.choice(["Rojo", "Azul"]) for _ in range(len(votantes))]
    return votos, posiciones[:len(votos)]

def mostrar_2_votos(votos, ventana, fuente):
    # Seleccionar dos votos aleatorios
    if len(votos) < 2:
        return

    votos_mostrados = random.sample(votos, 2)

    # Calcular las posiciones para los votos seleccionados
    posiciones_mostradas = [(150, 120 + i * 50) for i in range(2)]

    for voto, posicion in zip(votos_mostrados, posiciones_mostradas):
        texto = fuente.render(voto, True, (0, 0, 0))
        ventana.blit(texto, posicion)

    pygame.display.update()
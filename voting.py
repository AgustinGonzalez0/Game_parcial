import random
import pygame
from animaciones import mostrar_animacion_azul, mostrar_animacion_roja

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
    texto = f"Rojo: {votos.count('Rojo')}, Azul: {votos.count('Azul')}"
    print(texto)  # Añadir impresión de depuración
    texto_votos = fuente.render(texto, True, (0, 0, 0))
    ventana.blit(texto_votos, (100, 100))
    pygame.display.update()

def mostrar_animacion_votos(votantes, ventana):
    for i, votante in enumerate(votantes):
        if votante['decision'] == "Azul":
            mostrar_animacion_azul(ventana, posiciones[i])
        else:
            mostrar_animacion_roja(ventana, posiciones[i])
import random
import pygame

votantes = ["Votante 1", "Votante 2", "Votante 3", "Votante 4", "Votante 5"]

def generar_votos():
    return [random.choice(["Rojo", "Azul"]) for _ in range(len(votantes))] #cambiemos esto, es para ir mejorando 

def mostrar_2_votos(votos, ventana, fuente):
    indices = random.sample(range(len(votantes)), 2)
    for i in indices:
        texto_voto = fuente.render(f"{votantes[i]} votó: {votos[i]}", True, (0, 0, 0))
        ventana.blit(texto_voto, (100, 400 + 50 * i))
    pygame.display.update()
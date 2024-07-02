import sys
import pygame
import time
from voting import *

# Inicializar Pygame
pygame.init()

# Definir colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Configurar la pantalla
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Animación de Votos")

# Fuente para el texto del botón
font = pygame.font.Font(None, 36)

# Cargar las imágenes para la animación
voto_azul_paths = [
    "bandera azul/vote_azul(1).png",
    "bandera azul/vote_azul(2).png",
    "bandera azul/vote_azul(3).png",
    "bandera azul/vote_azul(4).png"
]
voto_rojo_paths = [
    "bandera roja/vote_rojo(1).png",
    "bandera roja/vote_rojo(2).png",
    "bandera roja/vote_rojo(3).png",
    "bandera roja/vote_rojo(4).png"
]

voto_azul = [pygame.image.load(path) for path in voto_azul_paths]
voto_rojo = [pygame.image.load(path) for path in voto_rojo_paths]

# Definir el rectángulo del botón
button_rect = pygame.Rect(300, 250, 200, 50)

def draw_button(screen, color, rect, text):
    pygame.draw.rect(screen, color, rect)
    text_surf = font.render(text, True, BLACK)
    text_rect = text_surf.get_rect(center=rect.center)
    screen.blit(text_surf, text_rect)

def mostrar_animacion_azul(screen, posiciones):
    for _ in range(5):  # Mostrar 5 ciclos de animación
        frame = int(time.time() * 5) % len(voto_azul)
        for posicion in posiciones:
            screen.blit(voto_azul[frame], posiciones)
        pygame.display.update()
        time.sleep(0.1)

def mostrar_animacion_roja(screen, posiciones):
    for _ in range(5):  # Mostrar 5 ciclos de animación
        frame = int(time.time() * 5) % len(voto_rojo)
        for posicion in posiciones:
            screen.blit(voto_rojo[frame], posiciones)
        pygame.display.update()
        time.sleep(0.1)

# ejecución del juego
import pygame
from game import start, game_data
from menu import *
pygame.init()  # Inicializar Pygame

if __name__ == "__main__":
    while True:
        accion = menu_principal()
        if accion == "iniciar":
            start()
        elif accion == "quit":
            break

pygame.quit()  # Finalizar Pygame
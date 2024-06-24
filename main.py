# ejecucion del juego

import pygame
from game import start, game_data

pygame.init()  # Inicializar Pygame

if __name__ == "__main__":
    # Iniciar el juego
    start()

pygame.quit()  # Finalizar Pygame
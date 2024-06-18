import pygame
from game import Game


pygame.init()  # Inicializar Pygame

if __name__ == "__main__":
    juego = Game()  # Crear instancia del juego
    juego.start()  # Iniciar el juego

pygame.quit()  # Finalizar Pygame
import pygame
from game import Game

def main():
    pygame.init()
    game = Game()
    game.start()
    pygame.quit()

if __name__ == "__main__":
    main()
    
    #usamos las importaciones de game y el main lo usamos para poder reproducir el juego
    #nose como vamos a crear la parte grafica, asi que veremos como lo hacemos
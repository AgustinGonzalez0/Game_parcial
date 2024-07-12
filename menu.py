import pygame
import game

pygame.init()
ventana = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Menu Principal")

def menu_principal():
    fondo_menu = pygame.image.load("wallpaperbetter.com_800x600_1.jpg")
    pygame.mixer.music.load("img_aud/Y2meta.app - Jujutsu Kaisen ; OP.4 (TV Size) _ Specialz _ Sub. Español & Romaji (AMV) (128 kbps).mp3")
    pygame.mixer.music.play(-1)

    fuente = pygame.font.Font(None, 74)
    opciones = ["Iniciar", "Salir"]
    seleccionado = 0

    while True:
        ventana.blit(fondo_menu, (0, 0))

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                return

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP:
                    seleccionado = (seleccionado - 1) % len(opciones)
                elif evento.key == pygame.K_DOWN:
                    seleccionado = (seleccionado + 1) % len(opciones)
                elif evento.key == pygame.K_RETURN:
                    if opciones[seleccionado] == "Iniciar":
                        game.start()
                        return  # Salir del bucle del menú para iniciar el juego
                    elif opciones[seleccionado] == "Salir":
                        pygame.quit()
                        return

        for i, opcion in enumerate(opciones):
            if i == seleccionado:
                texto = fuente.render(opcion, True, (255, 0, 0))
            else:
                texto = fuente.render(opcion, True, (0, 0, 0))
            ventana.blit(texto, (300, 200 + i * 100))

        pygame.display.flip()
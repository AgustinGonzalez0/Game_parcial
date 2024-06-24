#import pygame
#import sys
#import time

# Inicializar Pygame


# Definir colores
#WHITE = (255, 255, 255)
#BLACK = (0, 0, 0)
#GREEN = (0, 255, 0)
#RED = (255, 0, 0)

# Configurar la pantalla


# Fuente para el texto del botón
#font = pygame.font.Font(None, 36)

# Cargar las imágenes para la animación
#voto_azul_paths = (
#    "programacion_posta/voto_azul/vote_azul(1).png",
#    "programacion_posta/voto_azul/vote_azul(2).png",
#    "programacion_posta/voto_azul/vote_azul(3).png",
#    "programacion_posta/voto_azul/vote_azul(4).png"
#)
#voto_azul = [pygame.image.load(path) for path in voto_azul_paths]

# Definir el rectángulo del botón
#button_rect = pygame.Rect(300, 250, 200, 50)

#def draw_button(screen, color, rect, text):
#    pygame.draw.rect(screen, color, rect)
#    text_surf = font.render(text, True, BLACK)
#    text_rect = text_surf.get_rect(center=rect.center)
#    screen.blit(text_surf, text_rect)

#def main():
#    running = True

#    while running:
#        screen.fill(WHITE)
#        for event in pygame.event.get():
#            if event.type == pygame.QUIT:
#                running = False
#            elif event.type == pygame.MOUSEBUTTONDOWN:
#                if button_rect.collidepoint(event.pos):
#                    print("Botón presionado!")

        # Animación
#        frame = int(time.time() * 5) % len(voto_azul)
#        screen.blit(voto_azul[frame], (100, 100))

        # Detección del mouse para cambiar el color del botón
#        mouse_pos = pygame.mouse.get_pos()
#        if button_rect.collidepoint(mouse_pos):
#            button_color = GREEN
#        else:
#            button_color = RED

        # Dibujar el botón
#        draw_button(screen, button_color, button_rect, "Click Me")

 #       pygame.display.flip()

 #   pygame.quit()
 #   sys.exit()

#if __name__ == "__main__":
#    main()

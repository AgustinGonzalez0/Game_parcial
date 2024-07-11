import pygame

pygame.init()

# Cargar la imagen de fondo
fondo_menu = pygame.image.load('wallpaperbetter.com_800x600_1.jpg')

def mostrar_fondo_menu(ventana):
    ventana.blit(fondo_menu, (0, 0))

def menu_principal():
    ventana = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("ESTO O AQUELLO")
    fuente = pygame.font.Font(None, 50)
    reloj = pygame.time.Clock()

    botones = [
        pygame.Rect(300, 200, 200, 50),  # Iniciar
        pygame.Rect(300, 300, 200, 50)   # Salir
    ]
    textos = ["Iniciar", "Salir"]

    indice_seleccionado = 0

    corriendo = True
    while corriendo:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return "quit"
            if evento.type == pygame.MOUSEBUTTONDOWN:
                for i, boton in enumerate(botones):
                    if boton.collidepoint(evento.pos):
                        if i == 0:
                            return "iniciar"
                        elif i == 1:
                            return "quit"
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_DOWN:
                    indice_seleccionado = (indice_seleccionado + 1) % len(botones)
                elif evento.key == pygame.K_UP:
                    indice_seleccionado = (indice_seleccionado - 1) % len(botones)
                elif evento.key == pygame.K_RETURN:
                    if indice_seleccionado == 0:
                        return "iniciar"
                    elif indice_seleccionado == 2:
                        return "quit"

        # Mostrar el fondo del menú
        mostrar_fondo_menu(ventana)

        # Obtener la posición del ratón
        pos_raton = pygame.mouse.get_pos()

        # Función para dibujar botones con colores dinámicos
        def dibujar_boton(boton, texto, pos_texto, seleccionado):
            if boton.collidepoint(pos_raton) or seleccionado:
                pygame.draw.rect(ventana, (255, 255, 255), boton)
                texto_render = fuente.render(texto, True, (0, 0, 0))
            else:
                pygame.draw.rect(ventana, (0, 0, 0), boton)
                texto_render = fuente.render(texto, True, (255, 255, 255))
            ventana.blit(texto_render, pos_texto)

        # Dibujar los botones
        for i, boton in enumerate(botones):
            seleccionado = (i == indice_seleccionado)
            dibujar_boton(boton, textos[i], (boton.x + 50, boton.y + 10), seleccionado)
        pygame.display.flip()
        reloj.tick(60)

if __name__ == "__main__":
    menu_principal()
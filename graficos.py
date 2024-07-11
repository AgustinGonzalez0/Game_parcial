import pygame

# Definir colores
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
BLANCO = (255, 255, 255)

# Cargar y escalar la imagen del escenario
escenario = pygame.image.load('wallpaperbetter.com_800x600.jpg')
escenario = pygame.transform.scale(escenario, (800, 800))

def mostrar_escenario(ventana):
    ventana.blit(escenario, (0, 0))
    pygame.display.update()

def mostrar_grafico(ventana, fuente, votos, mostrar_porcentajes=False):
    print(f"Votos recibidos en mostrar_grafico: {votos}")  # Añadir impresión de depuración
    total = len(votos)
    if total == 0:  # Verificar si hay votos para evitar división por cero
        print("Error: No se han recibido votos.")
        return
    votos_rojo = votos.count("Rojo")
    votos_azul = votos.count("Azul")
    porcentaje_rojo = (votos_rojo / total) * 100
    porcentaje_azul = (votos_azul / total) * 100

    pygame.draw.rect(ventana, ROJO, (150, 500, 200, 30))
    pygame.draw.rect(ventana, AZUL, (450, 500, 200, 30))

    if mostrar_porcentajes:
        texto_rojo = fuente.render(f"{porcentaje_rojo:.2f}%", True, BLANCO)
        texto_azul = fuente.render(f"{porcentaje_azul:.2f}%", True, BLANCO)

        ventana.blit(texto_rojo, (150, 500))
        ventana.blit(texto_azul, (500, 500))

    pygame.display.update()

def mostrar_pregunta(ventana, fuente, pregunta, opciones):
    ventana.fill(BLANCO)
    ventana.blit(escenario, (0, 0))

    texto_pregunta = fuente.render(pregunta, True, NEGRO)
    ventana.blit(texto_pregunta, (345, 195))

    opcion_rojo_rect = pygame.Rect(50, 290, 295, 50)
    opcion_azul_rect = pygame.Rect(440, 290, 300, 50)

    texto_opcion_rojo = fuente.render(opciones[0], True, BLANCO)
    texto_opcion_azul = fuente.render(opciones[1], True, BLANCO)

    pygame.draw.rect(ventana, ROJO, opcion_rojo_rect)
    pygame.draw.rect(ventana, AZUL, opcion_azul_rect)

    ventana.blit(texto_opcion_rojo, (opcion_rojo_rect.x + 50, opcion_rojo_rect.y + 10))
    ventana.blit(texto_opcion_azul, (opcion_azul_rect.x + 50, opcion_azul_rect.y + 10))

    pygame.display.update()

def crear_boton(ventana, fuente, texto, color, rect):
    pygame.draw.rect(ventana, color, rect)
    texto_boton = fuente.render(texto, True, BLANCO)
    texto_rect = texto_boton.get_rect(center=((rect[0] + rect[2] / 2), (rect[1] + rect[3] / 2)))
    ventana.blit(texto_boton, texto_rect)
    pygame.display.update()
    return pygame.Rect(rect)
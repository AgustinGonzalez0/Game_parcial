import pygame

# Definir colores
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
AZUL_CLARO = (0, 150, 255)
BLANCO = (255, 255, 255)

# Cargar y escalar la imagen del escenario
escenario = pygame.image.load('_829b3046-c7bc-481e-b6fa-1d5eb27da4fd.png')
escenario = pygame.transform.scale(escenario, (800, 600))

def mostrar_escenario(ventana):
    ventana.blit(escenario, (0, 0))  # Dibujar la imagen del escenario en la ventana
    pygame.display.update()  # Actualizar pantalla

def mostrar_grafico(ventana, fuente, votos):
    total = len(votos)  # Total de votos
    votos_rojo = votos.count("Rojo")  # Votos para "Rojo"
    votos_azul = votos.count("Azul")  # Votos para "Azul"
    porcentaje_rojo = (votos_rojo / total) * 100  # Porcentaje de votos para "Rojo"
    porcentaje_azul = (votos_azul / total) * 100  # Porcentaje de votos para "Azul"

    # Dibujar el gráfico
    pygame.draw.rect(ventana, ROJO, (150, 500, 200, 30))  # Rectángulo rojo
    pygame.draw.rect(ventana, AZUL, (450, 500, 200, 30))  # Rectángulo azul

    texto_rojo = fuente.render(f"Rojo: {porcentaje_rojo:.2f}%", True, BLANCO)  # Texto del porcentaje rojo
    texto_azul = fuente.render(f"Azul: {porcentaje_azul:.2f}%", True, BLANCO)  # Texto del porcentaje azul

    ventana.blit(texto_rojo, (150, 500))  # Mostrar texto rojo
    ventana.blit(texto_azul, (450, 500))  # Mostrar texto azul
    pygame.display.update()  # Actualizar pantalla

def mostrar_pregunta(ventana, fuente, pregunta, opciones):
    ventana.blit(escenario, (0, 0))  # Dibujar la imagen del escenario en la ventana

    # Mostrar pregunta en la pantalla superior
    texto_pregunta = fuente.render(pregunta, True, NEGRO)
    pregunta_rect = texto_pregunta.get_rect(center=(400, 200))  # Ajustar según la posición de la pantalla superior
    ventana.blit(texto_pregunta, pregunta_rect.topleft)

    # Mostrar opción roja en la pantalla izquierda
    texto_opcion_rojo = fuente.render(f"{opciones[0]}", True, ROJO)
    opcion_rojo_rect = texto_opcion_rojo.get_rect(center=(150, 250))  # Ajustar según la posición de la pantalla izquierda
    ventana.blit(texto_opcion_rojo, opcion_rojo_rect.topleft)

    # Mostrar opción azul en la pantalla derecha
    texto_opcion_azul = fuente.render(f"{opciones[1]}", True, AZUL)
    opcion_azul_rect = texto_opcion_azul.get_rect(center=(650, 250))  # Ajustar según la posición de la pantalla derecha
    ventana.blit(texto_opcion_azul, opcion_azul_rect.topleft)

    pygame.display.update()  # Actualizar pantalla

def crear_boton(ventana, fuente, texto, color, rect):
    pygame.draw.rect(ventana, color, rect)  # Dibujar el rectángulo del botón
    texto_boton = fuente.render(texto, True, BLANCO)  # Renderizar el texto del botón
    texto_rect = texto_boton.get_rect(center=((rect[0] + rect[2] / 2), (rect[1] + rect[3] / 2)))  # Posición del texto en el botón
    ventana.blit(texto_boton, texto_rect)  # Dibujar el texto del botón
    pygame.display.update()  # Actualizar pantalla
    return pygame.Rect(rect)  # Devolver el rectángulo del botón

import pygame

# Definir colores
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
AZUL_CLARO = (0, 150, 255)
BLANCO = (255, 255, 255)

class Graficos:
    def __init__(self, ventana, fuente):
        self.ventana = ventana  # Ventana del juego
        self.fuente = fuente  # Fuente para el texto
        self.escenario = pygame.image.load('_829b3046-c7bc-481e-b6fa-1d5eb27da4fd.png')  # Cargar imagen del escenario
        self.escenario = pygame.transform.scale(self.escenario, (800, 600))  # Escalar la imagen al tamaño de la ventana

    def mostrar_grafico(self, votos):
        total = len(votos)  # Total de votos
        votos_rojo = votos.count("Rojo")  # Votos para "Rojo"
        votos_azul = votos.count("Azul")  # Votos para "Azul"
        porcentaje_rojo = (votos_rojo / total) * 100  # Porcentaje de votos para "Rojo"
        porcentaje_azul = (votos_azul / total) * 100  # Porcentaje de votos para "Azul"

        # Dibujar el gráfico
        pygame.draw.rect(self.ventana, ROJO, (150, 500, 200, 30))  # Rectángulo rojo
        pygame.draw.rect(self.ventana, AZUL, (450, 500, 200, 30))  # Rectángulo azul

        texto_rojo = self.fuente.render(f"Rojo: {porcentaje_rojo:.2f}%", True, BLANCO)  # Texto del porcentaje rojo
        texto_azul = self.fuente.render(f"Azul: {porcentaje_azul:.2f}%", True, BLANCO)  # Texto del porcentaje azul

        self.ventana.blit(texto_rojo, (150, 500))  # Mostrar texto rojo
        self.ventana.blit(texto_azul, (450, 500))  # Mostrar texto azul

    def mostrar_pregunta(self, pregunta, opciones):
        self.ventana.blit(self.escenario, (0, 0))  # Dibujar la imagen del escenario en la ventana

        # Mostrar pregunta en la pantalla superior
        texto_pregunta = self.fuente.render(pregunta, True, NEGRO)
        pregunta_rect = texto_pregunta.get_rect(center=(411, 200))  # Ajustar según la posición de la pantalla superior
        self.ventana.blit(texto_pregunta, pregunta_rect.topleft)

        # Mostrar opción roja en la pantalla izquierda
        texto_opcion_rojo = self.fuente.render(f"Rojo: {opciones[0]}", True, ROJO)
        opcion_rojo_rect = texto_opcion_rojo.get_rect(center=(150, 250))  # Ajustar según la posición de la pantalla izquierda
        self.ventana.blit(texto_opcion_rojo, opcion_rojo_rect.topleft)

        # Mostrar opción azul en la pantalla derecha
        texto_opcion_azul = self.fuente.render(f"Azul: {opciones[1]}", True, AZUL)
        opcion_azul_rect = texto_opcion_azul.get_rect(center=(600, 250))  # Ajustar según la posición de la pantalla derecha
        self.ventana.blit(texto_opcion_azul, opcion_azul_rect.topleft)

        pygame.display.update()  # Actualizar pantalla

    def crear_boton(self, texto, color, posicion, tamano):
        boton = pygame.Rect(*posicion, *tamano)  # Crear rectángulo para el botón
        pygame.draw.rect(self.ventana, color, boton)  # Dibujar botón
        texto_boton = self.fuente.render(texto, True, BLANCO)  # Crear texto del botón
        self.ventana.blit(texto_boton, (posicion[0] + 10, posicion[1] + 10))  # Mostrar texto del botón
        return boton  # Retornar el rectángulo del botón para detección de clics

    def mostrar_escenario(self):
        self.ventana.blit(self.escenario, (0, 0))  # Dibujar la imagen del escenario en la ventana
        pygame.display.update()  # Actualizar pantalla

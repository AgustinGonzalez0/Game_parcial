import pygame
import time
from questions import obtener_preguntas
from voting import generar_votos, mostrar_2_votos

# Definir colores
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
AZUL_CLARO = (0, 150, 255)
BLANCO = (255, 255, 255)

class Game:
    def __init__(self):
        self.ventana = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("ESTO O AQUELLO")
        self.fuente = pygame.font.Font(None, 36)
        self.comodines_usados = {"Next": False, "Half": False, "Reload": False}
        self.nivel = 0
        self.premio = 0
        self.tiempo_maximo = 15
        self.banco_preguntas = obtener_preguntas()
        
    def mostrar_grafico(self, votos):
        total = len(votos)
        votos_rojo = votos.count("Rojo")
        votos_azul = votos.count("Azul")
        porcentaje_rojo = (votos_rojo / total) * 100
        porcentaje_azul = (votos_azul / total) * 100

        # Dibujar el gráfico
        pygame.draw.rect(self.ventana, ROJO, (150, 500, 200, 30))
        pygame.draw.rect(self.ventana, AZUL, (450, 500, 200, 30))

        texto_rojo = self.fuente.render(f"Rojo: {porcentaje_rojo:.2f}%", True, BLANCO)
        texto_azul = self.fuente.render(f"Azul: {porcentaje_azul:.2f}%", True, BLANCO)

        self.ventana.blit(texto_rojo, (150, 500))
        self.ventana.blit(texto_azul, (450, 500))

    def mostrar_pregunta(self, pregunta, opciones):
        self.ventana.fill(AZUL_CLARO)
        texto_pregunta = self.fuente.render(pregunta, True, NEGRO)
        self.ventana.blit(texto_pregunta, (100, 100))

        texto_opcion_rojo = self.fuente.render(f"Rojo: {opciones[0]}", True, ROJO)
        texto_opcion_azul = self.fuente.render(f"Azul: {opciones[1]}", True, AZUL)

        self.ventana.blit(texto_opcion_rojo, (100, 200))
        self.ventana.blit(texto_opcion_azul, (100, 300))

        pygame.display.update()

    def usar_comodin(self, comodin, votos):
        if comodin == "Next":
            return True
        elif comodin == "Half":
            mostrar_2_votos(votos, self.ventana, self.fuente)
            return False
        elif comodin == "Reload":
            return True, generar_votos()
        return False

    def start(self):
        while self.nivel < len(self.banco_preguntas):
            pregunta_actual = self.banco_preguntas[self.nivel]
            votos = generar_votos()

            self.mostrar_pregunta(pregunta_actual["pregunta"], pregunta_actual["opciones"])
            self.mostrar_grafico(votos)

            inicio_tiempo = time.time()
            decision = None

            while (time.time() - inicio_tiempo) < self.tiempo_maximo:
                for evento in pygame.event.get():
                    if evento.type == pygame.QUIT:
                        pygame.quit()
                        return
                    if evento.type == pygame.KEYDOWN:
                        if evento.key == pygame.K_r:
                            decision = "Rojo"
                        elif evento.key == pygame.K_b:
                            decision = "Azul"
                        elif evento.key == pygame.K_n:
                            if not self.comodines_usados["Next"]:
                                self.comodines_usados["Next"] = True
                                decision = "Next"
                        elif evento.key == pygame.K_h:
                            if not self.comodines_usados["Half"]:
                                self.comodines_usados["Half"] = True
                                mostrar_2_votos(votos, self.ventana, self.fuente)
                        elif evento.key == pygame.K_l:
                            if not self.comodines_usados["Reload"]:
                                self.comodines_usados["Reload"] = True
                                votos = generar_votos()
                                self.mostrar_pregunta(pregunta_actual["pregunta"], pregunta_actual["opciones"])
                                self.mostrar_grafico(votos)

                if decision:
                    break

            if decision is None:
                print("Tiempo agotado. Fin del juego.")
                break

            if decision in ["Next", "Half", "Reload"]:
                if decision == "Next":
                    self.nivel += 1
                    self.premio += 100
                    continue
            elif decision in ["Rojo", "Azul"]:
                if decision == max(set(votos), key=votos.count):
                    print("¡Correcto!")
                    self.nivel += 1
                    self.premio += 100
                else:
                    print("Incorrecto. Fin del juego.")
                    break
            else:
                print("Opción inválida. Fin del juego.")
                break

        print(f"Premio total: ${self.premio}")

#vamos a usar esta parte para el apartado de la pantalla y configuracion del juego, ya vamos a ir manejando el tema con mas detalle
#pero usamos esto como base para ir empezando
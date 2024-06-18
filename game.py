import pygame
import time
from questions import obtener_preguntas
from voting import generar_votos, mostrar_2_votos
from graficos import Graficos

class Game:
    def __init__(self):
        self.ventana = pygame.display.set_mode((800, 600))  # Crear ventana del juego
        pygame.display.set_caption("ESTO O AQUELLO")  # Título de la ventana
        self.fuente = pygame.font.Font(None, 36)  # Fuente para el texto
        self.graficos = Graficos(self.ventana, self.fuente)  # Instancia de la clase Graficos
        self.comodines_usados = {"Next": False, "Half": False, "Reload": False}  # Estado de uso de comodines
        self.nivel = 0  # Nivel actual
        self.premio = 0  # Premio acumulado
        self.tiempo_maximo = 15  # Tiempo máximo para responder
        self.banco_preguntas = obtener_preguntas()  # Obtener banco de preguntas

    def usar_comodin(self, comodin, votos):
        if comodin == "Next":
            return True  # El comodín "Next" permite avanzar automáticamente
        elif comodin == "Half":
            mostrar_2_votos(votos, self.ventana, self.fuente)  # Muestra dos votos aleatorios
            return False
        elif comodin == "Reload":
            return True, generar_votos()  # Cambia la pregunta y los votos
        return False

    def start(self):
        self.graficos.mostrar_escenario()  # Mostrar escenario al inicio del juego

        while self.nivel < len(self.banco_preguntas):  # Mientras haya preguntas
            pregunta_actual = self.banco_preguntas[self.nivel]  # Pregunta actual
            votos = generar_votos()  # Generar votos aleatorios

            self.graficos.mostrar_pregunta(pregunta_actual["pregunta"], pregunta_actual["opciones"])  # Mostrar pregunta
            self.graficos.mostrar_grafico(votos)  # Mostrar gráfico de votos

            inicio_tiempo = time.time()  # Tiempo de inicio
            decision = None  # Decisión del jugador

            while (time.time() - inicio_tiempo) < self.tiempo_maximo:  # Mientras no se agote el tiempo
                for evento in pygame.event.get():
                    if evento.type == pygame.QUIT:  # Si se cierra la ventana
                        pygame.quit()
                        return
                    if evento.type == pygame.KEYDOWN:  # Si se presiona una tecla
                        if evento.key == pygame.K_r:
                            decision = "Rojo"  # Opción "Rojo"
                        elif evento.key == pygame.K_b:
                            decision = "Azul"  # Opción "Azul"
                        elif evento.key == pygame.K_n:
                            if not self.comodines_usados["Next"]:
                                self.comodines_usados["Next"] = True
                                decision = "Next"  # Comodín "Next"
                        elif evento.key == pygame.K_h:
                            if not self.comodines_usados["Half"]:
                                self.comodines_usados["Half"] = True
                                mostrar_2_votos(votos, self.ventana, self.fuente)  # Comodín "Half"
                        elif evento.key == pygame.K_l:
                            if not self.comodines_usados["Reload"]:
                                self.comodines_usados["Reload"] = True
                                votos = generar_votos()  # Comodín "Reload"
                                self.graficos.mostrar_pregunta(pregunta_actual["pregunta"], pregunta_actual["opciones"])  # Mostrar nueva pregunta
                                self.graficos.mostrar_grafico(votos)  # Mostrar nuevo gráfico de votos

                if decision:
                    break  # Salir del bucle si hay una decisión

            if decision is None:
                print("Tiempo agotado. Fin del juego.")
                break  # Terminar el juego si se agota el tiempo

            if decision in ["Next", "Half", "Reload"]:
                if decision == "Next":
                    self.nivel += 1  # Avanzar al siguiente nivel
                    self.premio += 100  # Aumentar el premio
                    continue
            elif decision in ["Rojo", "Azul"]:
                if decision == max(set(votos), key=votos.count):
                    print("¡Correcto!")
                    self.nivel += 1  # Avanzar al siguiente nivel
                    self.premio += 100  # Aumentar el premio
                else:
                    print("Incorrecto. Fin del juego.")
                    break  # Terminar el juego si la respuesta es incorrecta
            else:
                print("Opción inválida. Fin del juego.")
                break  # Terminar el juego si la opción es inválida

            print(f"Premio total: ${self.premio}")  # Mostrar el premio total al final del juego

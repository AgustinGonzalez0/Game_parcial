import pygame
import time
from questions import obtener_preguntas
from voting import generar_votos, mostrar_2_votos
import graficos
from animaciones import mostrar_animacion_azul # Importar las funciones de animación

# Inicializar Pygame
pygame.init()

# Definir datos del juego
game_data = {
    'ventana': pygame.display.set_mode((800, 600)),  # Ventana del juego
    'fuente': pygame.font.Font(None, 36),  # Fuente del juego
    'comodines_usados': {"Next": False, "Half": False, "Reload": False},  # Estado de los comodines
    'nivel': 0,  # Nivel del juego
    'premio': 0,  # Premio acumulado
    'tiempo_maximo': 15,  # Tiempo máximo por pregunta
    'banco_preguntas': obtener_preguntas(),  # Banco de preguntas
    'premios': [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],  # Premios por nivel
}

# Establecer título de la ventana
pygame.display.set_caption("ESTO O AQUELLO")

def usar_comodin(comodin, votos):
    if comodin == "Next":
        return True, votos
    elif comodin == "Half":
        mostrar_2_votos(votos, game_data['ventana'], game_data['fuente'])
        return False, votos
    elif comodin == "Reload":
        return True, generar_votos()
    return False, votos

def start():
    graficos.mostrar_escenario(game_data['ventana'])  # Mostrar el escenario inicial

    while game_data['nivel'] < len(game_data['banco_preguntas']):
        pregunta_actual = game_data['banco_preguntas'][game_data['nivel']]  # Pregunta actual
        votos = generar_votos()  # Generar votos aleatorios

        graficos.mostrar_pregunta(game_data['ventana'], game_data['fuente'], pregunta_actual["pregunta"], pregunta_actual["opciones"])  # Mostrar la pregunta
        graficos.mostrar_grafico(game_data['ventana'], game_data['fuente'], votos)  # Mostrar gráfico de votos

        boton_rojo = graficos.crear_boton(game_data['ventana'], game_data['fuente'], "Rojo", (255, 0, 0), (150, 400, 100, 50))  # Crear botón rojo
        boton_azul = graficos.crear_boton(game_data['ventana'], game_data['fuente'], "Azul", (0, 0, 255), (550, 400, 100, 50))  # Crear botón azul
        boton_next = graficos.crear_boton(game_data['ventana'], game_data['fuente'], "Next", (0, 150, 0), (650, 20, 100, 50))  # Crear botón Next
        boton_half = graficos.crear_boton(game_data['ventana'], game_data['fuente'], "Half", (150, 0, 150), (650, 80, 100, 50))  # Crear botón Half
        boton_reload = graficos.crear_boton(game_data['ventana'], game_data['fuente'], "Reload", (150, 150, 0), (650, 140, 100, 50))  # Crear botón Reload

        inicio_tiempo = time.time()  # Tiempo de inicio de la pregunta
        decision = None  # Decisión del jugador

        while (time.time() - inicio_tiempo) < game_data['tiempo_maximo']:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    return

                if evento.type == pygame.MOUSEBUTTONDOWN:
                    if boton_rojo.collidepoint(evento.pos):  # Verificar si se hizo clic en el botón rojo
                        decision = "Rojo"
                    elif boton_azul.collidepoint(evento.pos):  # Verificar si se hizo clic en el botón azul
                        decision = "Azul"
                    elif boton_next.collidepoint(evento.pos):  # Verificar si se hizo clic en el botón Next
                        if not game_data['comodines_usados']["Next"]:
                            game_data['comodines_usados']["Next"] = True
                            decision = "Next"
                    elif boton_half.collidepoint(evento.pos):  # Verificar si se hizo clic en el botón Half
                        if not game_data['comodines_usados']["Half"]:
                            game_data['comodines_usados']["Half"] = True
                            mostrar_2_votos(votos, game_data['ventana'], game_data['fuente'])
                    elif boton_reload.collidepoint(evento.pos):  # Verificar si se hizo clic en el botón Reload
                        if not game_data['comodines_usados']["Reload"]:
                            game_data['comodines_usados']["Reload"] = True
                            votos = generar_votos()
                            graficos.mostrar_pregunta(game_data['ventana'], game_data['fuente'], pregunta_actual["pregunta"], pregunta_actual["opciones"])
                            graficos.mostrar_grafico(game_data['ventana'], game_data['fuente'], votos)

            if decision:
                break

        if decision is None:
            print("Tiempo agotado. Fin del juego.")
            break

        if decision == "Next":
            game_data['nivel'] += 1
            game_data['premio'] += game_data['premios'][game_data['nivel'] - 1]
            continue
        elif decision == "Half" or decision == "Reload":
            continue
        elif decision in ["Rojo", "Azul"]:
            respuesta_correcta = max(set(votos), key=votos.count)  # Determinar la opción más votada

            # Mostrar la animación correspondiente
            #agregar aca la animacion roja con lo siguiente = if decision == "Roja":
            if decision == "Azul": #pasas la animacion azul a elif
                mostrar_animacion_azul(game_data['ventana'])

            # Mostrar los porcentajes de votos
            graficos.mostrar_grafico(game_data['ventana'], game_data['fuente'], votos, mostrar_porcentajes=True)
            time.sleep(5)  # Mostrar resultados por 5 segundos

            if decision == respuesta_correcta:
                print("¡Correcto!")
                game_data['nivel'] += 1
                game_data['premio'] += game_data['premios'][game_data['nivel'] - 1]
            else:
                print("Incorrecto. Fin del juego.")
                break
        else:
            print("Opción inválida. Fin del juego.")
            break

        print(f"Premio total: ${game_data['premio']}")

    pygame.quit()

if __name__ == "__main__":
    start()

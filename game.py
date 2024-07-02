from turtle import position
import pygame
import time
from questions import obtener_preguntas
from voting import generar_votos_con_posiciones, mostrar_2_votos
import graficos
from animaciones import *

# Iniciar Pygame
pygame.init()

game_data = {
    'ventana': pygame.display.set_mode((800, 600)),  
    'fuente': pygame.font.Font(None, 36),  
    'comodines_usados': {"Next": False, "Half": False, "Reload": False}, 
    'nivel': 0,  
    'premio': 0, 
    'tiempo_maximo': 15,  
    'banco_preguntas': obtener_preguntas(),  
    'preguntas_usadas': set(),
    'premios': [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],  
}

pygame.display.set_caption("ESTO O AQUELLO")

def manejar_pregunta(game_data):
    while True:
        pregunta_actual = game_data['banco_preguntas'][game_data['nivel']]
        if game_data['nivel'] not in game_data['preguntas_usadas']:
            break
        game_data['nivel'] += 1

    votos, posiciones = generar_votos_con_posiciones()

    graficos.mostrar_pregunta(game_data['ventana'], game_data['fuente'], pregunta_actual["pregunta"], pregunta_actual["opciones"])  # Mostrar la pregunta
    graficos.mostrar_grafico(game_data['ventana'], game_data['fuente'], votos)

    boton_rojo = graficos.crear_boton(game_data['ventana'], game_data['fuente'], "Rojo", (255, 0, 0), (150, 400, 100, 50))  # botón rojo
    boton_azul = graficos.crear_boton(game_data['ventana'], game_data['fuente'], "Azul", (0, 0, 255), (550, 400, 100, 50))  # botón azul
    boton_next = graficos.crear_boton(game_data['ventana'], game_data['fuente'], "Next", (0, 150, 0), (650, 20, 100, 50))  # Next
    boton_half = graficos.crear_boton(game_data['ventana'], game_data['fuente'], "Half", (150, 0, 150), (650, 80, 100, 50))  # Half
    boton_reload = graficos.crear_boton(game_data['ventana'], game_data['fuente'], "Reload", (150, 150, 0), (650, 140, 100, 50))  # Reload

    inicio_tiempo = time.time()  
    decision = None  
    while (time.time() - inicio_tiempo) < game_data['tiempo_maximo']:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                return "quit"

            if evento.type == pygame.MOUSEBUTTONDOWN:
                if boton_rojo.collidepoint(evento.pos):  
                    decision = "Rojo"
                elif boton_azul.collidepoint(evento.pos):  
                    decision = "Azul"
                elif boton_next.collidepoint(evento.pos):  
                    if not game_data['comodines_usados']["Next"]:
                        game_data['comodines_usados']["Next"] = True
                        decision = "Next"
                elif boton_half.collidepoint(evento.pos):  
                    if not game_data['comodines_usados']["Half"]:
                        game_data['comodines_usados']["Half"] = True
                        mostrar_2_votos(votos, game_data['ventana'], game_data['fuente'])
                elif boton_reload.collidepoint(evento.pos):  
                    if not game_data['comodines_usados']["Reload"]:
                        game_data['comodines_usados']["Reload"] = True
                        decision = "Reload"

        if decision:
            break

    if decision == None:
        print("Tiempo agotado. Fin del juego.")
        return "timeout"

    if decision == "Next":
        game_data['preguntas_usadas'].add(game_data['nivel'])
        return "next"
    elif decision == "Reload":
        return "reload"
    elif decision == "Half" or decision == "Reload":
        return "retry"
    elif decision == "Rojo" or decision == "Azul":
        respuesta_correcta = max(set(votos), key=votos.count)

        posiciones_azul = [pos for pos, voto in zip(posiciones, votos) if voto == "Azul"]
        posiciones_rojo = [pos for pos, voto in zip(posiciones, votos) if voto == "Rojo"]

        if decision == "Azul":
            for pos in posiciones_azul:
                mostrar_animacion_azul(game_data['ventana'], pos)
        elif decision == "Rojo":
            for pos in posiciones_rojo:
                mostrar_animacion_roja(game_data['ventana'], pos)

        graficos.mostrar_grafico(game_data['ventana'], game_data['fuente'], votos, mostrar_porcentajes=True)
        time.sleep(5)  

        if decision == respuesta_correcta:
            print("¡Correcto!")
            return "correct"
        else:
            print("Incorrecto. Fin del juego.")
            return "incorrect"
    else:
        print("Opción inválida. Fin del juego.")
        return "invalid"

def start():
    graficos.mostrar_escenario(game_data['ventana']) 

    while game_data['nivel'] < len(game_data['banco_preguntas']):
        resultado = manejar_pregunta(game_data)

        if resultado == "quit":
            break
        elif resultado == "timeout" or resultado == "incorrect" or resultado == "invalid":
            break
        elif resultado == "next" or resultado == "reload":
            game_data['nivel'] += 1
            if resultado == "next":
                game_data['premio'] += game_data['premios'][game_data['nivel'] - 1]
        elif resultado == "correct":
            game_data['nivel'] += 1
            game_data['premio'] += game_data['premios'][game_data['nivel'] - 1]

        print(f"Premio total: ${game_data['premio']}")

    pygame.quit()

if __name__ == "__main__":
    start()

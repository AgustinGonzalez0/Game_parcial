import pygame
import time
from questions import banco_preguntas, get_random_pregunta
from voting import generar_votos_con_posiciones, mostrar_2_votos
import graficos
from animaciones import mostrar_animacion
from menu import menu_principal

# Iniciar Pygame
pygame.init()

game_data = {
    'ventana': pygame.display.set_mode((800, 600)),
    'fuente': pygame.font.Font(None, 25),
    'comodines_usados': {"Next": False, "Half": False, "Reload": False},
    'nivel': 0,
    'premio': 0,
    'tiempo_maximo': 15,
    'banco_preguntas': banco_preguntas,
    'preguntas_usadas': set(),
    'premios': [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],
}

pygame.display.set_caption("ESTO O AQUELLO")

def respuesta_correcta(votos):
    conteo_votos = {}
    for voto in votos:
        if voto in conteo_votos:
            conteo_votos[voto] += 1
        else:
            conteo_votos[voto] = 1

    voto_mas_frecuente = None
    max_ocurrencias = 0
    for voto, ocurrencias in conteo_votos.items():
        if ocurrencias > max_ocurrencias:
            max_ocurrencias = ocurrencias
            voto_mas_frecuente = voto

    return voto_mas_frecuente

def mostrar_puntaje(ventana, fuente, puntaje):
    texto_puntaje = fuente.render(f"Puntaje: ${puntaje}", True, (0, 0, 0))
    ventana.blit(texto_puntaje, (10, 10))

def mostrar_tiempo_restante(ventana, fuente, tiempo_restante, posicion):
    texto_tiempo = fuente.render(f"Tiempo restante: {int(tiempo_restante)}s", True, (255, 0, 0))
    ventana.blit(texto_tiempo, posicion)

def manejar_pregunta(game_data):
    while True:
        pregunta_actual = get_random_pregunta()
        pregunta_ya_usada = False

        # Verificar si el nivel actual ya se ha usado
        for pregunta_usada in game_data['preguntas_usadas']:
            if game_data['nivel'] == pregunta_usada:
                pregunta_ya_usada = True
                break

        if not pregunta_ya_usada:
            break
        game_data['nivel'] += 1

    votos, posiciones = generar_votos_con_posiciones()

    graficos.mostrar_pregunta(game_data['ventana'], game_data['fuente'], pregunta_actual["pregunta"], pregunta_actual["opciones"])  # Mostrar la pregunta
    graficos.mostrar_grafico(game_data['ventana'], game_data['fuente'], votos)
    mostrar_puntaje(game_data['ventana'], game_data['fuente'], game_data['premio'])

    boton_rojo = graficos.crear_boton(game_data['ventana'], game_data['fuente'], "Rojo", (255, 0, 0), (150, 400, 100, 50))  # botón rojo
    boton_azul = graficos.crear_boton(game_data['ventana'], game_data['fuente'], "Azul", (0, 0, 255), (550, 400, 100, 50))  # botón azul
    boton_next = graficos.crear_boton(game_data['ventana'], game_data['fuente'], "Next", (0, 150, 0), (650, 20, 100, 50))  # Next
    boton_half = graficos.crear_boton(game_data['ventana'], game_data['fuente'], "Half", (150, 0, 150), (650, 80, 100, 50))  # Half
    boton_reload = graficos.crear_boton(game_data['ventana'], game_data['fuente'], "Reload", (150, 150, 0), (650, 140, 100, 50))  # Reload

    inicio_tiempo = time.time()
    decision = None
    notify_comodin_use = lambda comodin: print(f"Comodín {comodin} usado.")

    while (time.time() - inicio_tiempo) < game_data['tiempo_maximo']:
        tiempo_restante = game_data['tiempo_maximo'] - (time.time() - inicio_tiempo)
        # Redibujar solo el tiempo restante
        pygame.draw.rect(game_data['ventana'], (255, 255, 255), (10, 50, 200, 30))  # Limpiar área del tiempo
        mostrar_tiempo_restante(game_data['ventana'], game_data['fuente'], tiempo_restante, (10, 50))

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
                        notify_comodin_use("Next")
                        decision = "Next"
                elif boton_half.collidepoint(evento.pos):
                    if not game_data['comodines_usados']["Half"]:
                        game_data['comodines_usados']["Half"] = True
                        notify_comodin_use("Half")
                        mostrar_2_votos(votos, game_data['ventana'], game_data['fuente'])
                elif boton_reload.collidepoint(evento.pos):
                    if not game_data['comodines_usados']["Reload"]:
                        game_data['comodines_usados']["Reload"] = True
                        notify_comodin_use("Reload")
                        decision = "Reload"

        pygame.display.update((10, 50, 200, 30))  # Actualizar solo el área del tiempo

        if decision:
            break

    if decision is None:
        print("Se te terminó el tiempo")
        return "timeout"

    if decision == "Next":
        game_data['premio'] += game_data['premios'][game_data['nivel']]
        game_data['preguntas_usadas'].add(game_data['nivel'])
        game_data['nivel'] += 1
        return "next"
    elif decision == "Reload":
        return "reload"
    elif decision == "Half":
        return "retry"
    elif decision == "Rojo" or decision == "Azul":
        respuesta = respuesta_correcta(votos)

        posiciones_azul = [pos for pos, voto in zip(posiciones, votos) if voto.lower() == "azul"]
        posiciones_rojo = [pos for pos, voto in zip(posiciones, votos) if voto.lower() == "rojo"]

        mostrar_animacion(game_data['ventana'], posiciones_rojo, posiciones_azul)

        graficos.mostrar_grafico(game_data['ventana'], game_data['fuente'], votos, mostrar_porcentajes=True)
        time.sleep(5)

        if decision == respuesta:
            print("¡Correcto!".title())
            return "correct".lower()
        else:
            print("Incorrecto. Fin del juego.".title())
            return "incorrect".lower()
    else:
        print("Opción inválida. Fin del juego.".title())
        return "invalid".lower()

def start():
    graficos.mostrar_escenario(game_data['ventana'])

    while game_data['nivel'] < len(game_data['banco_preguntas']):
        resultado = manejar_pregunta(game_data)

        if resultado == "quit":
            break
        elif resultado == "timeout" or resultado == "incorrect" or resultado == "invalid":
            break
        elif resultado == "next":
            continue
        elif resultado == "reload":
            continue
        elif resultado == "retry":
            continue
        elif resultado == "correct":
            game_data['premio'] += game_data['premios'][game_data['nivel']]
            game_data['nivel'] += 1

    print(f"Fin del juego. Puntaje final: ${game_data['premio']}")

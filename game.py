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
    # Crear una superficie temporal con un color con canal alfa
    ancho, alto = 200, 30
    superficie_opaca = pygame.Surface((ancho, alto))
    superficie_opaca.set_alpha(128)  # 128 es 50% de opacidad
    superficie_opaca.fill((255, 255, 255))  # Color blanco con opacidad

    # Dibujar la superficie temporal en la ventana principal
    ventana.blit(superficie_opaca, posicion)

    # Renderizar y dibujar el texto
    texto_tiempo = fuente.render(f"Tiempo restante: {int(tiempo_restante)}s", True, (255, 0, 0))
    ventana.blit(texto_tiempo, posicion)

def manejar_pregunta(game_data):
    while True:
        pregunta_actual = get_random_pregunta()
        pregunta_ya_usada = False

        for pregunta_usada in game_data['preguntas_usadas']:
            if game_data['nivel'] == pregunta_usada:
                pregunta_ya_usada = True
                break

        if not pregunta_ya_usada:
            break
        game_data['nivel'] += 1

    votos, posiciones = generar_votos_con_posiciones()

    graficos.mostrar_pregunta(game_data['ventana'], game_data['fuente'], pregunta_actual["pregunta"], pregunta_actual["opciones"])
    graficos.mostrar_grafico(game_data['ventana'], game_data['fuente'], votos)
    mostrar_puntaje(game_data['ventana'], game_data['fuente'], game_data['premio'])

    boton_rojo = graficos.crear_boton(game_data['ventana'], game_data['fuente'], "Rojo", (255, 0, 0), (150, 400, 100, 50))
    boton_azul = graficos.crear_boton(game_data['ventana'], game_data['fuente'], "Azul", (0, 0, 255), (550, 400, 100, 50))
    boton_next = graficos.crear_boton(game_data['ventana'], game_data['fuente'], "Next", (0, 255, 255), (650, 20, 100, 50))  # Aqua
    boton_half = graficos.crear_boton(game_data['ventana'], game_data['fuente'], "Half", (0, 0, 128), (650, 80, 100, 50))  # Navy Blue
    boton_reload = graficos.crear_boton(game_data['ventana'], game_data['fuente'], "Reload", (128, 128, 128), (650, 140, 100, 50))  # Gris

    inicio_tiempo = time.time()
    decision = None
    notify_comodin_use = lambda comodin: print(f"Comodín {comodin} usado.")

    while (time.time() - inicio_tiempo) < game_data['tiempo_maximo']:
        tiempo_restante = game_data['tiempo_maximo'] - (time.time() - inicio_tiempo)
        pygame.draw.rect(game_data['ventana'], (255, 255, 255), (10, 50, 200, 30))
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

        pygame.display.update((10, 50, 200, 30))

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

        graficos.mostrar_grafico(game_data['ventana'], game_data['fuente'], votos)
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

def mostrar_resultado(final_data, imagen, sonido):
    ventana = final_data['ventana']
    fuente = final_data['fuente']
    ventana.fill((255, 255, 255))  # Llenar la ventana con blanco
    imagen = pygame.image.load(imagen)
    imagen = pygame.transform.scale(imagen, (800, 600))
    ventana.blit(imagen, (0, 0))
    pygame.display.update()
    pygame.mixer.music.load(sonido)
    pygame.mixer.music.play()

def start():
    # Cargar música de fondo del juego
    pygame.mixer.music.load('img_aud/juego.mp3')
    pygame.mixer.music.play(-1)  # Reproducir en bucle

    graficos.mostrar_escenario(game_data['ventana'])

    while game_data['nivel'] < len(game_data['banco_preguntas']):
        resultado = manejar_pregunta(game_data)

        if resultado == "quit":
            break
        elif resultado == "timeout" or resultado == "incorrect" or resultado == "invalid":
            mostrar_resultado(game_data, 'img_aud/perdiste.png', 'img_aud/Y2meta.app - ESTO NO ES UN JUEGO _ EL XOKAS TWITCH (128 kbps).mp3')
            time.sleep(5)  # Esperar 5 segundos para mostrar la pantalla de pérdida
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

    if game_data['nivel'] >= len(game_data['banco_preguntas']):
        mostrar_resultado(game_data, 'img_aud/ganaste.png', 'img_aud/victoria.mp3')
        time.sleep(5)  # Esperar 5 segundos para mostrar la pantalla de victoria
    print(f"Fin del juego. Puntaje final: ${game_data['premio']}")
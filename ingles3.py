import pygame
import random

# Definir colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode([screen_width, screen_height])

# Configuración del título de la ventana
pygame.display.set_caption("Aprende inglés")

# Función para cargar preguntas desde la base de datos
def cargar_preguntas():
    preguntas = ["What is the capital of Spain?", "What is the past tense of 'eat'?", 
                 "What does 'feline' mean?", "How many planets are in our solar system?",
                 "What is the opposite of 'cold'?"]
    return preguntas

# Función para generar una pregunta aleatoria
def generar_pregunta():
    preguntas = cargar_preguntas()
    return random.choice(preguntas)

# Función para mostrar una pregunta en la pantalla
def mostrar_pregunta(pregunta):
    font = pygame.font.Font(None, 36)
    texto = font.render(pregunta, True, BLACK)
    screen.blit(texto, [screen_width/2 - texto.get_width()/2, screen_height/2 - texto.get_height()/2])

# Función para mostrar la puntuación actual en la pantalla
def mostrar_puntuacion(score, nivel):
    font = pygame.font.Font(None, 24)
    texto = font.render("Puntuación: " + str(score) + "   Nivel: " + str(nivel), True, BLACK)
    screen.blit(texto, [10, 10])

# Función para mostrar el mensaje de fin del juego en la pantalla
def mostrar_mensaje_final(score):
    font = pygame.font.Font(None, 36)
    texto = font.render("¡Fin del juego! Tu puntuación final es: " + str(score), True, BLACK)
    screen.blit(texto, [screen_width/2 - texto.get_width()/2, screen_height/2 - texto.get_height()/2])

# Función principal del juego
def juego():
    # Configurar variables del juego
    score = 0
    nivel = 1
    respuesta_correcta = False

    # Bucle principal del juego
    while not respuesta_correcta:
        # Generar una pregunta aleatoria
        pregunta = generar_pregunta()

        # Mostrar la pregunta y la puntuación actual en la pantalla
        mostrar_pregunta(pregunta)
        mostrar_puntuacion(score, nivel)

        # Esperar respuesta del usuario
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.unicode == "s":
                    respuesta_correcta = True
                    score += 1
                    nivel += 1
                elif event.unicode == "q":
                    respuesta_correcta = True

        # Actualizar la pantalla
        pygame.display.update()

    # Mostrar la puntuación final del jugador
    mostrar_mensaje_final(score)

    # Esperar a que el jugador cierre la ventana
    esperar_cierre = True
    while esperar_cierre:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                esperar_cierre = False

    # Salir del juego
    pygame.quit()

# Iniciar el juego
juego()

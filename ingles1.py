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
    preguntas = []
    # Lógica para cargar preguntas desde la base de datos
    return preguntas

# Función para generar una pregunta aleatoria
def generar_pregunta():
    preguntas = cargar_preguntas()
    return random.choice(preguntas)

# Función para mostrar una pregunta en la pantalla
def mostrar_pregunta(pregunta):
    font = pygame.font.Font(None, 36)
    texto = font.render(pregunta, True, BLACK)
    pantalla.blit(texto, [screen_width/2, screen_height/2])

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

        # Mostrar la pregunta en la pantalla
        mostrar_pregunta(pregunta)

        # Esperar respuesta del usuario
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.unicode == "s":
                    respuesta_correcta = True
                    score += 1
                    nivel += 1

        # Actualizar la pantalla
        pygame.display.update()

    # Mostrar la puntuación final del jugador
    font = pygame.font.Font(None, 36)
    texto = font.render("Tu puntuación final es: " + str(score), True, BLACK)
    pantalla.blit(texto, [screen_width/2, screen_height/2])

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

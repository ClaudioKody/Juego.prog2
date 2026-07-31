
import pygame

# Configuración de la pantalla
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
CAPTION = "Retro Arcade Shooter"
FPS = 60

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Inicialización de Pygame
pygame.init()
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(CAPTION)
CLOCK = pygame.time.Clock()

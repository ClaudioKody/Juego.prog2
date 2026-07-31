import pygame
from config import SCREEN_WIDTH, SCREEN_HEIGHT
from utils.constants import ENEMY_WIDTH, ENEMY_HEIGHT, ENEMY_SPEED

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        # Superficie transparente para dibujar al alienígena
        self.image = pygame.Surface((ENEMY_WIDTH, ENEMY_HEIGHT), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = ENEMY_SPEED
        
        self.draw_alien()

    def draw_alien(self):
        """Dibuja una abejita / alienígena retro."""
        self.image.fill((0, 0, 0, 0))
        w, h = ENEMY_WIDTH, ENEMY_HEIGHT
        
        # Cuerpo principal (Rojo/Naranja)
        pygame.draw.ellipse(self.image, (230, 50, 50), (4, 4, w - 8, h - 8))
        # Ojos amarillos
        pygame.draw.circle(self.image, (255, 230, 0), (w // 3, h // 3 + 2), 4)
        pygame.draw.circle(self.image, (255, 230, 0), (2 * w // 3, h // 3 + 2), 4)
        # Pupilas negras
        pygame.draw.circle(self.image, (0, 0, 0), (w // 3, h // 3 + 2), 2)
        pygame.draw.circle(self.image, (0, 0, 0), (2 * w // 3, h // 3 + 2), 2)
        # Antenas blancas
        pygame.draw.line(self.image, (255, 255, 255), (w // 3, 4), (w // 4, 0), 2)
        pygame.draw.line(self.image, (255, 255, 255), (2 * w // 3, 4), (3 * w // 4, 0), 2)

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()  # Eliminar enemigo si sale de la pantalla

    def shoot(self):
        # Esto será implementado por el patrón Factory
        pass
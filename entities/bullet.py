import pygame
from config import SCREEN_WIDTH, SCREEN_HEIGHT
from utils.constants import BULLET_WIDTH, BULLET_HEIGHT, BULLET_SPEED

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, direction, speed_x=0): # speed_x opcional para disparos diagonales
        super().__init__()
        self.image = pygame.Surface((BULLET_WIDTH, BULLET_HEIGHT), pygame.SRCALPHA)
        
        # Dibujamos un rayo láser neón (borde amarillo, centro cian brillante)
        self.image.fill((255, 255, 0))
        pygame.draw.rect(self.image, (0, 255, 230), (1, 1, BULLET_WIDTH - 2, BULLET_HEIGHT - 2))
        
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.speed_y = BULLET_SPEED * direction
        self.speed_x = speed_x  # Movimiento horizontal

    def update(self):
        # Mueve la bala en vertical y horizontal
        self.rect.y -= self.speed_y
        self.rect.x += self.speed_x
        
        # Elimina el proyectil si sale de la pantalla por cualquier borde
        if (self.rect.bottom < 0 or self.rect.top > SCREEN_HEIGHT or 
            self.rect.right < 0 or self.rect.left > SCREEN_WIDTH):
            self.kill()
            
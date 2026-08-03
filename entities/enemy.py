import pygame
import random
from config import SCREEN_WIDTH, SCREEN_HEIGHT
from utils.constants import ENEMY_WIDTH, ENEMY_HEIGHT, ENEMY_SPEED

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        # Damos un pequeño margen extra a la superficie para que los dibujos no queden apretados
        self.image = pygame.Surface((ENEMY_WIDTH + 6, ENEMY_HEIGHT + 6), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = ENEMY_SPEED
        self.direction = random.choice([-1, 1])  # Para que se muevan a los lados
        
        # Fijamos un objetivo de altura en la zona media de la pantalla (más abajo, bien visibles)
        self.target_y = random.randint(100, 240)

    def update(self):
        # 1. Si todavía no llegaron a la zona media, descienden suavemente
        if self.rect.y < self.target_y:
            self.rect.y += 2
        else:
            # 2. Una vez en posición, patrullan lateralmente de forma amenazante
            self.rect.x += self.speed * self.direction
            
            # Rebotar en los bordes laterales de la pantalla
            if self.rect.left <= 15 or self.rect.right >= SCREEN_WIDTH - 15:
                self.direction *= -1
                # Al rebotar, varían levemente su altura para dar dinamismo pero sin irse arriba
                self.rect.y += random.choice([-8, 8])
                self.rect.y = max(80, min(self.rect.y, 280))

    def draw_alien(self):
        pass


class EnemyTypeA(Enemy):
    """Enemigo 1: Tipo Abejita Roja"""
    def __init__(self, x, y):
        super().__init__(x, y)
        self.draw_alien()

    def draw_alien(self):
        self.image.fill((0, 0, 0, 0))
        w, h = self.rect.width, self.rect.height
        # Cuerpo rojo
        pygame.draw.ellipse(self.image, (230, 50, 50), (4, 4, w - 8, h - 8))
        # Ojos amarillos
        pygame.draw.circle(self.image, (255, 230, 0), (w // 3, h // 3 + 2), 4)
        pygame.draw.circle(self.image, (255, 230, 0), (2 * w // 3, h // 3 + 2), 4)
        pygame.draw.circle(self.image, (0, 0, 0), (w // 3, h // 3 + 2), 2)
        pygame.draw.circle(self.image, (0, 0, 0), (2 * w // 3, h // 3 + 2), 2)


class EnemyTypeB(Enemy):
    """Enemigo 2: Tipo Platillo Verde"""
    def __init__(self, x, y):
        super().__init__(x, y)
        self.speed = ENEMY_SPEED * 1.2  
        self.draw_alien()

    def draw_alien(self):
        self.image.fill((0, 0, 0, 0))
        w, h = self.rect.width, self.rect.height
        # Plato verde brillante
        pygame.draw.ellipse(self.image, (50, 230, 100), (2, h // 3, w - 4, h // 2))
        # Cúpula central azul
        pygame.draw.circle(self.image, (0, 150, 255), (w // 2, h // 3), 6)


class EnemyTypeC(Enemy):
    """Enemigo 3: Tipo Tanque Morado"""
    def __init__(self, x, y):
        super().__init__(x, y)
        self.speed = ENEMY_SPEED * 0.7  # Más lento pero imponente
        self.draw_alien()

    def draw_alien(self):
        self.image.fill((0, 0, 0, 0))
        w, h = self.rect.width, self.rect.height
        # Bloque principal morado
        pygame.draw.rect(self.image, (180, 50, 220), (4, 4, w - 8, h - 8), border_radius=4)
        # Ojos blancos amenazantes
        pygame.draw.line(self.image, (255, 255, 255), (6, 10), (w - 6, 10), 3)
        
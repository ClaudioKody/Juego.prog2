
from patterns.strategy.enemy_strategy import EnemyStrategy
from config import SCREEN_WIDTH

class ZigzagMovement(EnemyStrategy):
    def __init__(self):
        self.direction = 1 # 1 for right, -1 for left
        self.change_direction_threshold = 50 # Cambiar de dirección cada 50 píxeles en X
        self.current_x_movement = 0

    def execute(self, enemy):
        enemy.rect.y += enemy.speed // 2 # Moverse más lento verticalmente
        enemy.rect.x += enemy.speed * self.direction
        self.current_x_movement += enemy.speed * self.direction

        if abs(self.current_x_movement) >= self.change_direction_threshold:
            self.direction *= -1
            self.current_x_movement = 0

        # Asegurarse de que el enemigo no salga de la pantalla horizontalmente
        if enemy.rect.left < 0:
            enemy.rect.left = 0
            self.direction = 1
            self.current_x_movement = 0
        if enemy.rect.right > SCREEN_WIDTH:
            enemy.rect.right = SCREEN_WIDTH
            self.direction = -1
            self.current_x_movement = 0

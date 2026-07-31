
from patterns.strategy.enemy_strategy import EnemyStrategy

class SimpleMovement(EnemyStrategy):
    def execute(self, enemy):
        enemy.rect.y += enemy.speed

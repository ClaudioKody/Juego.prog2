
from patterns.factory.factory import AbstractFactory
from entities.enemy import Enemy

class EnemyFactory(AbstractFactory):
    def create_product(self, x, y):
        return Enemy(x, y)

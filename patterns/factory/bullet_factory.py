
from patterns.factory.factory import AbstractFactory
from entities.bullet import Bullet

class BulletFactory(AbstractFactory):
    def create_product(self, x, y, direction):
        return Bullet(x, y, direction)

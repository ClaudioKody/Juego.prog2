
from abc import ABC, abstractmethod

class PlayerDecorator(ABC):
    def __init__(self, player):
        self._player = player

    @abstractmethod
    def update(self):
        self._player.update()

    @abstractmethod
    def draw(self, screen):
        self._player.draw(screen)

    @abstractmethod
    def shoot(self):
        self._player.shoot()

class DoubleShotDecorator(PlayerDecorator):
    def __init__(self, player):
        super().__init__(player)

    def shoot(self):
        # Lógica para doble disparo
        print("Doble disparo!")
        self._player.shoot() # Disparo original
        # Añadir un segundo disparo

    def update(self):
        self._player.update()

    def draw(self, screen):
        self._player.draw(screen)

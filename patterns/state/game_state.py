
from abc import ABC, abstractmethod

class GameState(ABC):
    def __init__(self, game):
        self.game = game

    @abstractmethod
    def enter(self):
        pass

    @abstractmethod
    def exit(self):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def draw(self, screen):
        pass

    @abstractmethod
    def handle_event(self, event):
        pass

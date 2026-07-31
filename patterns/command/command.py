
from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class MoveLeftCommand(Command):
    def __init__(self, player):
        self.player = player

    def execute(self):
        self.player.move_left()

class MoveRightCommand(Command):
    def __init__(self, player):
        self.player = player

    def execute(self):
        self.player.move_right()

class ShootCommand(Command):
    def __init__(self, player):
        self.player = player

    def execute(self):
        self.player.shoot()

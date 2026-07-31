
from abc import ABC, abstractmethod

class EnemyStrategy(ABC):
    @abstractmethod
    def execute(self, enemy):
        pass

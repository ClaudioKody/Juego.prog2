
from abc import ABC, abstractmethod

class AbstractFactory(ABC):
    @abstractmethod
    def create_product(self, *args, **kwargs):
        pass

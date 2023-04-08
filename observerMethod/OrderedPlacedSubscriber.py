import abc
from abc import ABC

class OrderPlacedSubscriber(ABC):
    @abc.abstractmethod
    def orderPlaced(self):
        pass


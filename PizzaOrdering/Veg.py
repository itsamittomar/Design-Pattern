import abc
class Vegetarian(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def getCost(self):
        pass

    @abc.abstractmethod
    def getDescription(self):
        pass

    @abc.abstractmethod
    def getTopping(self):
        pass

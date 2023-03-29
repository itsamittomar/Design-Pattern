from abc import ABC, abstractclassmethod

class TicketFactory(ABC):

    def __init__(self) -> None:
        super().__init__()

    @abstractclassmethod
    def createdrink():
        pass

    @abstractclassmethod
    def createfood():
        pass

    @abstractclassmethod
    def createseat():
        pass

    
from abc import ABC, abstractclassmethod

class Seat(ABC):
    def __init__(self) -> None:
        super().__init__()
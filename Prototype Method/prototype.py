import abc
from typing import Protocol

# class prototype(metaclass = abc.ABCMeta):
#     @abc.abstractmethod
#     def clone():
#         pass 

class prototype(Protocol):
    def clone(self):
        pass


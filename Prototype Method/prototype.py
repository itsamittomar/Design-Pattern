import abc

class prototype(metaclass = abc.ABCMeta):
    @abc.abstractmethod
    def clone():
        pass 
    

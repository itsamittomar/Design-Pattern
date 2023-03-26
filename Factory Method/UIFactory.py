from typing import Protocol

class UIFactory(Protocol):
    def createMenu():
        pass

    def createDropDown():
        pass 

    def createButton():
        pass

    
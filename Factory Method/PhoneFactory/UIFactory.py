from typing import Protocol

class UIFactory(Protocol):
    def createMenu(self):
        pass

    def createDropDown(self):
        pass 

    def createButton(self):
        pass

    
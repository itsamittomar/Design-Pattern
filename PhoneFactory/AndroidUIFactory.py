from UIFactory import UIFactory
from Component.Button import AndroidButton
from Component.Dropdown import AndroidDropDown
from Component.Menu import AndroidMenu


class AndroidUIFactory(UIFactory):
    def createMenu(self):
        return AndroidMenu()
    
    def createButton(self):
        return AndroidButton()
    
    def createDropDown(self):
        return AndroidDropDown()


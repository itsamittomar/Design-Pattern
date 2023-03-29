from UIFactory import UIFactory
from Component.Button import WindowsButton
from Component.Dropdown import WindowsDropDown
from Component.Menu import windowMenu

class WindowsUIFactory(UIFactory):
    def createMenu(self):
        return windowMenu()

    def createButton(self):
        return WindowsButton()
    
    def createDropDown(self):
        return WindowsDropDown()
    

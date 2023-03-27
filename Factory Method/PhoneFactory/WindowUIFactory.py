from UIFactory import UIFactory
import Component.Button.WindowsButton as Button
import Component.Dropdown.WindowsDropDown as DropDown
import Component.Menu.windowMenu as Menu

class WindowsUIFactory(UIFactory):
    def createMenu(self):
        return Menu()

    def createButton(self):
        return Button()
    
    def createDropDown(self):
        return DropDown()
    

from UIFactory import UIFactory
import Component.Button.WindowsButton as Button
import Component.Dropdown.WindowsDropDown as DropDown
import Component.Menu.windowMenu as Menu

class WindowsUIFactory(UIFactory):
    def createMenu():
        return Menu()

    def createButton():
        return Button()
    
    def createDropDown():
        return DropDown()
    

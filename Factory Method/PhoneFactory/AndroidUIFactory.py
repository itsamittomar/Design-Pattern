from UIFactory import UIFactory
import Component.Menu.AndroidMenu as AndroidMenu
import Component.Button.AndroidButton as AndroidButton
import Component.Dropdown.AndroidDropDown as AndroidDropDown

class AndroidUIFactory(UIFactory):
    def createMenu(self):
        return AndroidMenu()
    
    def createButton(self):
        return AndroidButton()
    
    def createDropDown(self):
        return AndroidDropDown()


from UIFactory import UIFactory
import Component.Menu.AndroidMenu as AndroidMenu
import Component.Button.AndroidButton as AndroidButton
import Component.Dropdown.AndroidDropDown as AndroidDropDown

class AndroidUIFactory(UIFactory):
    def createMenu():
        return AndroidMenu()
    
    def createButton():
        return AndroidButton()
    
    def createDropDown():
        return AndroidDropDown()


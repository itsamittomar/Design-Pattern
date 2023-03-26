from UIFactory import UIFactory
import Component.Button.IOSButton as IOSBUtton
import Component.Dropdown.IOSDropDown as IOSDropDown
import Component.Menu.IOSMenu as IOSMenu 


class IOSUIFactory(UIFactory):
    def createMenu():
        return IOSMenu()
    
    def createButton():
        return IOSBUtton()

    def createDropDown():
        return IOSDropDown()
    

from UIFactory import UIFactory
import Component.Button.IOSButton as IOSButton
import Component.Dropdown.IOSDropDown as IOSDropDown
import Component.Menu.IOSMenu as IOSMenu 


class IOSUIFactory(UIFactory):
    def createMenu(self):
        return IOSMenu()
    
    def createButton(self):
        return IOSButton()

    def createDropDown(self):
        return IOSDropDown()
    

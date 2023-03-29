from UIFactory import UIFactory
from Component.Button import IOSButton
from Component.Dropdown import IOSDropDown
from Component.Menu import IOSMenu


class IOSUIFactory(UIFactory):
    def createMenu(self):
        return IOSMenu()
    
    def createButton(self):
        return IOSButton()

    def createDropDown(self):
        return IOSDropDown()
    

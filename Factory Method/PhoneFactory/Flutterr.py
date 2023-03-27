from UIFactoryFactory import UIFactoryFactory


class Flutterr:
    def __int__(self, platform):
        self.platform = platform

    @staticmethod
    def setTheme():
        print("Setting the theme")

    @staticmethod
    def setRefreshRate():
        print("Setting the refresh rate for the Application")

    def createUiFactory(self):
        return UIFactoryFactory.createUIFactory(self.platform)

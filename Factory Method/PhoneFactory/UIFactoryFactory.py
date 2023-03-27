from typing import Optional
from AndroidUIFactory import AndroidUIFactory
from IOSUIFactory import IOSUIFactory
from WindowUIFactory import WindowsUIFactory
from SupportedPlatform import SupportedPlatform
from UIFactory import UIFactory


class UIFactoryFactory:

    @staticmethod
    def createUIFactory(supportedPlatform: SupportedPlatform) -> Optional[UIFactory]:
        if supportedPlatform == SupportedPlatform.Android:
            return AndroidUIFactory()

        elif supportedPlatform == SupportedPlatform.Windows:
            return WindowsUIFactory()

        elif supportedPlatform == SupportedPlatform.IOS:
            return IOSUIFactory()
        else:
            return None

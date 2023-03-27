from Flutterr import Flutterr
from SupportedPlatform import SupportedPlatform


def main():
    flutter = Flutterr(SupportedPlatform.Android)
    uiFactory = flutter.createUiFactory()
    menu = uiFactory.createMenu()
    button = uiFactory.createButton()
    dropdown = uiFactory.createDropDown()
    print(flutter)


if __name__ == '__main__':
    main()


import sys
print(sys.path)
from PhoneFactory.Flutterr import flutterr as F
from PhoneFactory.SupportedPlatform import SupportedPlatform as S


def main():
    flutter = F.flutterr(S.SupportedPlatform.Android)
    uiFactory = flutter.createUiFactory()
    menu = uiFactory.createMenu()
    button = uiFactory.createButton()
    dropdown = uiFactory.createDropDown()
    print(flutter)


if __name__ == '__main__':
    main()

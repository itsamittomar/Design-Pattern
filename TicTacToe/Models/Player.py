from TicTacToe.Models.Move import Move
from TicTacToe.Models.PlayerType import PlayerType
from TicTacToe.Models.cell import cell
class Player:
    _name =""
    _symbol = ""
    _playerType = PlayerType()

    def __init__(self,name,symbol,playerType):
        self._name = name
        self._symbol = symbol
        self._playerType = playerType

    def decide_move(self):
        #
        print("Enter the row and col")
        num = input().split()
        return Move(self,cell(num[0],num[1]))

    def getName(self):
        return self._name

    def setName(self,name):
        self._name = name

    def getSymbol(self):
        return self._symbol

    def setSymbol(self,symbol):
        self._symbol = symbol

    def getPlayerType(self):
        return self._playerType

    def setPlayerType(self,typePlayer):
        self._playerType = typePlayer




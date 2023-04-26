from TicTacToe.Models.Player import Player
from TicTacToe.Models.cellState import cellState


class Move:
    _cell = cellState()

    def __init__(self, player, cell):
        self._player = player
        self._cell = cell

    def getPlayer(self):
        return self._player

    def setPlayer(self,player):
        self._player = player

    def getCell(self):
        return self._cell

    def setCell(self,cell):
        self._cell = cell


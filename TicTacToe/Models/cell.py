from TicTacToe.Models.cellState import cellState


class cell:
    _cellState = cellState()

    def __init__(self, row, col):
        self._row = row
        self._col = col
        self._cellState = self._cellState.EMPTY

    def getRow(self):
        return self._row

    def setRow(self, row):
        self._row = row

    def getCol(self):
        return self._col

    def setCol(self, col):
        self._col = col

    def getCellState(self):
        return self._cellState

    def setCellState(self, cellval):
        self._cellState = cellval

    def getPlayer(self):
        return self._player

    def setPlayer(self, player):
        self._player = player

import TicTacToe.Models
from TicTacToe.Models.cell import cell
from TicTacToe.Models.cellState import cellState


class Board:
    board = []

    def __init__(self, dimension):
        self.dimension = dimension
        for i in range(dimension):
            self.board.append([])
            for j in range(dimension):
                self.board[i].append(cell(i, j))

    def display(self):
        for i in range(self.dimension):
            for j in range(self.dimension):
                if self.board[i][j].getCellState() == cellState.EMPTY:
                    print("|   |")
                else:
                    print("|" + self.board[i][j].getPlayer().getSymbol() + "|")

    def getboard(self):
        return self.board

    def setBoard(self, newBoard):
        self.board = newBoard


if __name__ == '__main__':
    Board(3)

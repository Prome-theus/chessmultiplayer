from piece import camel
from piece import king
from piece import rock
from piece import pawn
from piece import queen
from piece import horse


class Board:
    rect = (50, 50, 593, 592)
    startX = rect[0]
    startY = rect[1]

    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols

        self.board = [[0 for x in range(8)] for _ in range(rows)]

        self.board[0][0] = rock(0, 0, "b")
        self.board[0][1] = horse(0, 1, "b")
        self.board[0][2] = camel(0, 2, "b")
        self.board[0][3] = queen(0, 3, "b")
        self.board[0][4] = king(0, 4, "b")
        self.board[0][5] = camel(0, 5, "b")
        self.board[0][6] = horse(0, 6, "b")
        self.board[0][7] = rock(0, 7, "b")

        self.board[1][0] = pawn(1, 0, "b")
        self.board[1][1] = pawn(1, 1, "b")
        self.board[1][2] = pawn(1, 2, "b")
        self.board[1][3] = pawn(1, 3, "b")
        self.board[1][4] = pawn(1, 4, "b")
        self.board[1][5] = pawn(1, 5, "b")
        self.board[1][6] = pawn(1, 6, "b")
        self.board[1][7] = pawn(1, 7, "b")

        self.board[7][0] = rock(7, 0, "w")
        self.board[7][1] = horse(7, 1, "w")
        self.board[7][2] = camel(7, 2, "w")
        self.board[7][3] = queen(7, 3, "w")
        self.board[7][4] = king(7, 4, "w")
        self.board[7][5] = camel(7, 5, "w")
        self.board[7][6] = horse(7, 6, "w")
        self.board[7][7] = rock(7, 7, "w")

        self.board[6][0] = pawn(6, 0, "w")
        self.board[6][1] = pawn(6, 1, "w")
        self.board[6][2] = pawn(6, 2, "w")
        self.board[6][3] = pawn(6, 3, "w")
        self.board[6][4] = pawn(6, 4, "w")
        self.board[6][5] = pawn(6, 5, "w")
        self.board[6][6] = pawn(6, 6, "w")
        self.board[6][7] = pawn(6, 7, "w")



    def draw(self, win, board):
        for i in range(self.rows):
            for j in range (self.cols):
                if self.board[i][j] != 0:
                     self.board[i][j].draw(win, board)

    def select(self, col, row):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j] != 0:
                    self.board[i][j].selected = False

        if self.board[row][col] != 0:
            self.board[row][col].selected = True

    def move(self, start, end):
        removed = self.board[end[1]][end[0]]
        self.board[end[1]][end[0]] = self.board[start[1]][start[0]]
        self.board[start[1]][start[0]] = 0
        return removed
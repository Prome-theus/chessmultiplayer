import pygame
import os

PATH = os.path.abspath('.') + '/'

b_camel = pygame.image.load(PATH + '/chess/bcamel.png')
b_horse = pygame.image.load(PATH + 'chess/bhorse.png')
b_king = pygame.image.load(PATH + 'chess/bking.png')
b_queen = pygame.image.load(PATH + 'chess/bqueen.png')
b_pawn = pygame.image.load(PATH + 'chess/bpawn.png')
b_rock = pygame.image.load(PATH + 'chess/brock.png')

camel = pygame.image.load(PATH + 'chess/camel.png')
king = pygame.image.load(PATH + 'chess/king.png')
queen = pygame.image.load(PATH + 'chess/queen.png')
rock = pygame.image.load(PATH + 'chess/rock.png')
pawn = pygame.image.load(PATH + 'chess/pawn.png')
horse = pygame.image.load(PATH + 'chess/horse.png')

b = [b_camel, b_king, b_horse, b_pawn, b_queen, b_rock]
w = [camel, king, horse, pawn, queen, rock]

B = []
W = []

for img in b:
    B.append(pygame.transform.scale(img, (60, 60)))

for img in w:
    W.append(pygame.transform.scale(img, (60, 60)))


class piece:
    img = -1
    rect = (50, 50, 593, 592)
    startX = rect[0]
    startY = rect[1]

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.selected = False

    def valid_moves(self, board):
        pass

    def isSelected(self):
        return self.selected

    def draw(self, win, board):
        if self.color == "w":
            drawthis = W[self.img]
        else:
            drawthis = B[self.img]

        if self.selected:
            moves = self.valid_moves(board)

            for move in moves:
                x = 33 + round(self.startX + (move[0] * self.rect[2] / 8))
                y = 33 + round(self.startY + (move[1] * self.rect[3] / 8))
                pygame.draw.circle(win, (255, 0, 0), (x, y), 10)

        x = 5 + round(self.startX + (self.col * self.rect[2] / 8))
        y = 5 + round(self.startY + (self.row * self.rect[3] / 8))

        if self.selected:
            pygame.draw.rect(win, (255, 0, 0), (x, y, 63, 63), 2)

        win.blit(drawthis, (x, y))


class camel(piece):
    img = 0

    def valid_moves(self, board):
        return []


class king(piece):
    img = 1

    def valid_moves(self, board):
        i = self.row
        j = self.col

        moves = []
        # topleft
        if i > 0:
            if j > 0:
                moves.append((j - 1, i - 1))

            # topmiddle
            moves.append((j, i - 1))

            # topright
            if j < 7:
                moves.append((j + 1, i - 1))

        if i < 7:
            # bottomleft
            if j > 0:
                moves.append((j - 1, i + 1))

            # bottommiddle
            moves.append((j, i + 1))

            # bottomright
            if j < 7:
                moves.append((j + 1, i + 1))

        # left
        if j > 0:
            moves.append((j - 1, i))
        # right
        if j < 7:
            moves.append((j + 1, i))
        return moves


class horse(piece):
    img = 2

    def valid_moves(self, board):
        i = self.row
        j = self.col

        moves = []
        # down left
        if i < 5 and j > 0:
            p = board[i + 2][j - 1]
            if p == 0:
                moves.append((j - 1, i + 2))
        # up left
        if i > 1 and j > 0:
            p = board[i - 2][j - 1]
            if p == 0:
                moves.append((j - 1, i - 2))
        # down right
        if i < 6 and j < 7:
            p = board[i + 2][j + 1]
            if p == 0:
                moves.append((j + 1, i + 2))

        # up right
        if i > 6 and j < 7:
            p = board[i - 2][j + 1]
            if p == 0:
                moves.append((j + 1, i - 2))

        return moves


class pawn(piece):
    img = 3

    def __init__(self, row, col, color):
        super().__init__(row, col, color)
        self.first = True
        self.queen = False

    def valid_moves(self, board):
        i = self.row
        j = self.col

        moves = []
        if self.first:
            if i < 6:
                p = board[i + 2][j]
                if p == 0:
                    moves.append((j, i + 2))

            if i < 7:
                p = board[i + 1][j]
                if p == 0:
                    moves.append((j, i + 1))
        return moves


class queen(piece):
    img = 4

    def valid_moves(self, board):
        # i = self.row
        # j = self.col
        #
        # moves = []
        #
        # #up right diagonal
        # currentcol = j
        # currentrow = i
        # for row in range(0, 8):
        #     if currentcol - 1 >= 0:
        #         m1 = board[row][currentcol-1]
        #     if currentcol + 1 <= 7:
        #         m2 = board[row][currentcol-1]
        #
        #     currentcol += 1
        return []


class rock(piece):
    img = 5

    def valid_moves(self, board):
        i = self.row
        j = self.col

        moves = []

        # up
        for x in range(i, -1, -1):
            p = board[i][j]
            if p == 0:
                moves.append((j, x))
                break

        # down
        for x in range(i, 8, 1):
            p = board[i][j]
            if p == 0:
                moves.append((j, x))
                break

        # left
        for x in range(j, -1, -1):
            p = board[i][j]
            if p == 0:
                moves.append((x, i))
                break

        # right
        for x in range(j, 8, 1):
            p = board[i][j]
            if p == 0:
                moves.append((x, i))
                break
        return moves

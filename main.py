import pygame
import os
from board import Board

PATH = os.path.abspath('.') + '/'
board = pygame.transform.scale(pygame.image.load(PATH + 'board.png'),(693,693))
rect = (50, 50, 593, 592)


def redraw_gamewindow():
    global win, bo
    win.blit(board, (0, 0))
    bo.draw(win, board)
    pygame.display.update()


def click(pos):
    x = pos[0]
    y = pos[1]
    if rect[0] < x < rect[0] + rect[2]:
        if rect[1] < x < rect[1] + rect[3]:
            divX = x - rect[0]
            divY = y - rect[0]
            i = int(divX / (rect[2] / 8))
            j = int(divY / (rect[3] / 8))
            return i, j


def main():
    global bo
    bo = Board(8, 8)
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(10)
        redraw_gamewindow()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
                run = False
                pygame.quit()

            if event.type == pygame.MOUSEMOTION:
                pass
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                i, j = click(pos)
                # bo.board[i][j].selected = True
                bo.select(i, j)


width = 693
height = 693
win = pygame.display.set_mode((width, height), pygame.SCALED)
pygame.display.set_caption("Chess game")
main()

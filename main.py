import sys
import pygame
import numpy as np
from db import *

pygame.init()

screenttt = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TicTacToe AI")
screenttt.fill(BG_COLOR)
pygame.display.set_icon(pygame.image.load(ICON))


class Board():

    def __init__(self) -> None:
        self.squares = np.zeros((ROWS, COLS))

    def mask_sqr(self, row, col, player):
        self.squares[row][col] = player


class Game:
    def __init__(self, board) -> None:
        self.board = board()
        self.draw_lines()
        self.player = 1

    def draw_lines(self):
        pygame.draw.line(screenttt, LINE_COLOR,
                         (SQUARE_SIZE, 0), (SQUARE_SIZE, HEIGHT), LINE_WIDTH)
        pygame.draw.line(screenttt, LINE_COLOR,
                         (2*SQUARE_SIZE, 0), (2*SQUARE_SIZE, HEIGHT), LINE_WIDTH)

        pygame.draw.line(screenttt, LINE_COLOR,
                         (0, SQUARE_SIZE), (WIDTH, SQUARE_SIZE), LINE_WIDTH)
        pygame.draw.line(screenttt, LINE_COLOR,
                         (0, 2*SQUARE_SIZE), (WIDTH, 2*SQUARE_SIZE), LINE_WIDTH)


def main():

    game = Game()

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                row = pos[1] // SQUARE_SIZE
                col = pos[0] // SQUARE_SIZE
                if game.player == 1:
                    game.player = 2
                else:
                    game.player == 1
        pygame.display.update()


main()

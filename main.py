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

    def sq_empty(self, row, col):
        return self.squares[row][col] == 0


class Game:
    def __init__(self) -> None:
        self.board = Board()
        self.draw_lines()
        self.player = 1  # 1 => circle; 2 => cross

    def draw_lines(self) -> None:
        pygame.draw.line(screenttt, LINE_COLOR,
                         (SQSIZE, 0), (SQSIZE, HEIGHT), LINE_WIDTH)
        pygame.draw.line(screenttt, LINE_COLOR,
                         (2*SQSIZE, 0), (2*SQSIZE, HEIGHT), LINE_WIDTH)

        pygame.draw.line(screenttt, LINE_COLOR,
                         (0, SQSIZE), (WIDTH, SQSIZE), LINE_WIDTH)
        pygame.draw.line(screenttt, LINE_COLOR,
                         (0, 2*SQSIZE), (WIDTH, 2*SQSIZE), LINE_WIDTH)

    def draw_figure(self, row, col):
        if self.player == 1:
            # circle
            center = (col * SQSIZE + SQSIZE // 2,
                      row * SQSIZE + SQSIZE // 2)
            pygame.draw.circle(screenttt, CIRCLE_COLOR, center,
                               RADIUS, FIG_WIDTH)
        if self.player == 2:
            lup = (col * SQSIZE + OFFSET, row * SQSIZE + OFFSET)
            ldn = (col * SQSIZE + OFFSET, row * SQSIZE + 4*OFFSET)
            rup = (col * SQSIZE + 4*OFFSET, row * SQSIZE + OFFSET)
            rdn = (col * SQSIZE + 4*OFFSET, row * SQSIZE + 4*OFFSET)
            pygame.draw.line(screenttt, CROSS_COLOR, lup, rdn, FIG_WIDTH)
            pygame.draw.line(screenttt, CROSS_COLOR, ldn, rup, FIG_WIDTH)

    def next_turn(self):
        self.player = self.player % 2 + 1


def main():

    game = Game()
    board = game.board

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                row = pos[1] // SQSIZE
                col = pos[0] // SQSIZE

                if board.sq_empty(row, col):
                    board.squares[row][col] = game.player
                    game.draw_figure(row, col)
                    game.next_turn()

        pygame.display.update()


main()

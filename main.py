import sys
import pygame
import numpy as np
import random
import copy
from db import *

pygame.init()
screenttt = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TicTacToe AI")
screenttt.fill(BG_COLOR)
pygame.display.set_icon(pygame.image.load(ICON))


class Board():

    def __init__(self):
        self.squares = np.zeros((ROWS, COLS))
        self.empty_sqrs = self.squares
        self.marked_sqrs = 0

    def mark_sqr(self, row, col, player):
        self.squares[row][col] = player
        self.marked_sqrs += 1

    def sq_empty(self, row, col):
        return self.squares[row][col] == 0

    def get_empty(self):
        e_sqrs = []
        for row in range(ROWS):
            for col in range(COLS):
                if self.sq_empty(row, col):
                    e_sqrs.append((row, col))
        return e_sqrs

    def state(self):
        # vert wins
        for col in range(COLS):
            if self.squares[0][col] == self.squares[1][col] == self.squares[2][col] != 0:
                return self.squares[0][col]

        # horiz wins
        for row in range(ROWS):
            if self.squares[row][0] == self.squares[row][1] == self.squares[row][2] != 0:
                return self.squares[row][0]

        # diagonal wins
        if self.squares[0][0] == self.squares[1][1] == self.squares[2][2] != 0:
            # lup = (0 * SQSIZE + OFFSET, 0 * SQSIZE + OFFSET)
            # rdn = (2 * SQSIZE + 4*OFFSET, 2 * SQSIZE + 4*OFFSET)
            # pygame.draw.line(screenttt, CROSS_COLOR, lup, rdn, CRSS_WIDTH)
            return self.squares[0][0]

        if self.squares[0][2] == self.squares[1][1] == self.squares[2][0] != 0:
            # ldn = (0 * SQSIZE + OFFSET, 2 * SQSIZE + 4*OFFSET)
            # rup = (2 * SQSIZE + 4*OFFSET, 0 * SQSIZE + OFFSET)
            # pygame.draw.line(screenttt, CROSS_COLOR, ldn, rup, CRSS_WIDTH)
            return self.squares[1][1]
        # nothin yet
        return 0

    def isfull(self):
        return self.marked_sqrs == 9

    def isempty(self):
        return self.marked_sqrs == 0


class AI():
    def __init__(self, level=1, player=2):
        self.level = level
        self.player = player

    def rand_m(self, board):
        e_sqrs = board.get_empty()
        rnd = random.randrange(0, len(e_sqrs))

        return e_sqrs[rnd]  # -> (row, col)

    def minimax(self, board, maximize):

        case = board.state()

        if case == 1:
            return 1, None
        if case == 2:
            return -1, None
        elif board.isfull():
            return 0, None

        if maximize:
            max_eval = -2
            best_move = None
            e_sqrs = board.get_empty()

            for (row, col) in e_sqrs:
                temp_board = copy.deepcopy(board)
                temp_board.mark_sqr(row, col, 1)
                eval = self.minimax(temp_board, False)[0]
                if eval > max_eval:
                    max_eval = eval
                    best_move = (row, col)
            return max_eval, best_move

        elif not maximize:
            min_eval = 2
            best_move = None
            e_sqrs = board.get_empty()

            for (row, col) in e_sqrs:
                temp_board = copy.deepcopy(board)
                temp_board.mark_sqr(row, col, self.player)
                eval = self.minimax(temp_board, True)[0]
                if eval < min_eval:
                    min_eval = eval
                    best_move = (row, col)

            return min_eval, best_move

    def first_move(self, board):
        if (board.squares[0, 0] or
            board.squares[0, 2] or
            board.squares[2, 0] or
                board.squares[2, 2]):
            eval, move = 0, (1, 1)
        elif (board.squares[0, 1] or
              board.squares[1, 0] or
                board.squares[1, 1]):
            eval, move = 0, (0, 0)
        elif (board.squares[1, 2]):
            eval, move = 0, (0, 2)
        elif (board.squares[2, 1]):
            eval, move = 0, (0, 1)
        return eval, move

    def eval(self, main_board):
        if self.level == 0:
            eval = "random"
            move = self.rand_m(main_board)
        else:
            if (main_board.marked_sqrs == 1):
                eval, move = self.first_move(main_board)
            else:
                eval, move = self.minimax(main_board, False)

        print(
            f'AI has chosen to mark the square in pos {move} with an eval of: {eval}')

        return move


class Game:
    def __init__(self) -> None:
        self.board = Board()
        self.ai = AI()
        self.gamemode = "ai"
        self.running = True
        self.player = 1  # 1 => circle; 2 => cross

    def draw_board(self) -> None:
        screenttt.fill(BG_COLOR)
        pygame.draw.line(screenttt, LINE_COLOR,
                         (SQSIZE, 0), (SQSIZE, HEIGHT), LINE_WIDTH)
        pygame.draw.line(screenttt, LINE_COLOR,
                         (2*SQSIZE, 0), (2*SQSIZE, HEIGHT), LINE_WIDTH)

        pygame.draw.line(screenttt, LINE_COLOR,
                         (0, SQSIZE), (WIDTH, SQSIZE), LINE_WIDTH)
        pygame.draw.line(screenttt, LINE_COLOR,
                         (0, 2*SQSIZE), (WIDTH, 2*SQSIZE), LINE_WIDTH)

    def draw_figure(self, row, col):
        if self.player == 2:
            # circle
            center = (col * SQSIZE + SQSIZE // 2,
                      row * SQSIZE + SQSIZE // 2)
            pygame.draw.circle(screenttt, CIRCLE_COLOR, center,
                               RADIUS, CCLE_WIDTH)
        elif self.player == 1:
            lup = (col * SQSIZE + OFFSET, row * SQSIZE + OFFSET)
            ldn = (col * SQSIZE + OFFSET, row * SQSIZE + 4*OFFSET)
            rup = (col * SQSIZE + 4*OFFSET, row * SQSIZE + OFFSET)
            rdn = (col * SQSIZE + 4*OFFSET, row * SQSIZE + 4*OFFSET)
            pygame.draw.line(screenttt, CROSS_COLOR, lup, rdn, CRSS_WIDTH)
            pygame.draw.line(screenttt, CROSS_COLOR, ldn, rup, CRSS_WIDTH)

    def next_turn(self):
        self.player = self.player % 2 + 1

    def mark(self, row, col):
        self.board.mark_sqr(row, col, self.player)
        self.draw_figure(row, col)
        self.next_turn()


def main():

    game = Game()
    board = game.board
    ai = game.ai
    game.draw_board()

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_r]:
                game = Game()
                board = game.board
                ai = game.ai
                game.draw_board()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                row = pos[1] // SQSIZE
                col = pos[0] // SQSIZE

                if board.sq_empty(row, col) and board.state() == 0:
                    game.mark(row, col)

        if game.gamemode == "ai" and game.player == ai.player and not board.isfull() and board.state() == 0:
            pygame.display.update()

            row, col = ai.eval(board)
            game.mark(row, col)

        pygame.display.update()


main()

import sys
import pygame
import numpy as np
import random
import copy
import pyautogui
from db import *

pygame.init()
screenttt = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TicTacToe AI")
screenttt.fill(BG_COLOR)
pygame.display.set_icon(pygame.image.load(ICON))
clock = pygame.time.Clock()


class Board():

    def __init__(self):
        self.squares = np.zeros((ROWS, COLS))
        self.empty_sqrs = self.squares
        self.marked_sqrs = 0

    def mark_sqr(self, row, col, player):  # oznaceni policka
        self.squares[row][col] = player
        self.marked_sqrs += 1

    def sq_empty(self, row, col):  # kontrola jestli je pole prazdne
        return self.squares[row][col] == 0

    def get_empty(self):  # vrati seznam prazdnych poli
        e_sqrs = []
        for row in range(ROWS):
            for col in range(COLS):
                if self.sq_empty(row, col):
                    e_sqrs.append((row, col))
        return e_sqrs

    def state(self, show=False):  # kontroluje stav hry a zobrazuje vyherce
        # vert wins
        for col in range(COLS):
            if self.squares[0][col] == self.squares[1][col] == self.squares[2][col] != 0:
                if show:
                    color = CIRCLE_COLOR if self.squares[0][col] == 2 else CROSS_COLOR
                    sPos = (col * SQSIZE + SQSIZE // 2, 15)
                    fPos = (col * SQSIZE + SQSIZE // 2, HEIGHT - 15)
                    pygame.draw.line(screenttt, color, sPos,
                                     fPos, CRSS_WIDTH - 6)
                return self.squares[0][col]

        # horiz wins
        for row in range(ROWS):
            if self.squares[row][0] == self.squares[row][1] == self.squares[row][2] != 0:
                if show:
                    color = CIRCLE_COLOR if self.squares[row][0] == 2 else CROSS_COLOR
                    sPos = (15, row * SQSIZE + SQSIZE // 2)
                    fPos = (WIDTH - 15, row * SQSIZE + SQSIZE // 2)
                    pygame.draw.line(screenttt, color, sPos,
                                     fPos, CRSS_WIDTH - 6)
                return self.squares[row][0]

        # diagonal wins
        if self.squares[0][0] == self.squares[1][1] == self.squares[2][2] != 0:
            if show:
                color = CIRCLE_COLOR if self.squares[0][0] == 2 else CROSS_COLOR
                sPos = (15, 15)
                fPos = (WIDTH - 15, HEIGHT - 15)
                pygame.draw.line(screenttt, color, sPos, fPos, CRSS_WIDTH)
            return self.squares[0][0]

        if self.squares[0][2] == self.squares[1][1] == self.squares[2][0] != 0:
            if show:
                color = CIRCLE_COLOR if self.squares[1][1] == 2 else CROSS_COLOR
                sPos = (15, HEIGHT - 15)
                fPos = (WIDTH - 15, 15)
                pygame.draw.line(screenttt, color, sPos, fPos, CRSS_WIDTH)
            return self.squares[1][1]
        return 0

    def isfull(self):  # kontrola jestli jsou vsechna pole plna
        return self.marked_sqrs == 9

    def isempty(self):  # kontrola jestli jsou vsechna pole prazdna
        return self.marked_sqrs == 0

    def running(self):  # kontrola jestli hra ma stale bezet
        return not self.isfull() and self.state() == 0


class AI():
    def __init__(self, level=1, player=2):
        self.level = level
        self.player = player

    def rand_m(self, board):  # vybere nahodne pole
        e_sqrs = board.get_empty()
        rnd = random.randrange(0, len(e_sqrs))

        return e_sqrs[rnd]  # -> (row, col)

    def minimax(self, board, maximize):  # hlavni algoritmus n vyber nejlepsiho tahu

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

    # zrychleni algoritmu
    # jelikoz na zacatku neni moc moznosti
    def first_move(self, board):
        if (board.squares[0, 0] or
            board.squares[0, 2] or
            board.squares[2, 0] or
                board.squares[2, 2]):
            move = (1, 1)
        elif board.squares[0, 1]:
            moves = [(0, 0), (0, 2), (2, 1)]
            move = moves[random.randrange(0, 3)]
        elif board.squares[1, 0]:
            moves = [(0, 0), (2, 0), (1, 2)]
            move = moves[random.randrange(0, 3)]
        elif board.squares[1, 1]:
            moves = [(0, 0), (0, 2), (2, 0), (2, 2)]
            move = moves[random.randrange(0, 4)]
        elif board.squares[1, 2]:
            moves = [(0, 2), (1, 0), (2, 2)]
            move = moves[random.randrange(0, 3)]
        elif board.squares[2, 1]:
            moves = [(0, 1), (2, 0), (2, 2)]
            move = moves[random.randrange(0, 3)]
        return 0, move

    # pouzije hlavni algoritmus, zhodnoti, a vrati nejlepsi tah
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
    def __init__(self, gamemode="ai", aistr=1) -> None:
        self.board = Board()
        self.ai = AI(level=aistr)
        self.gamemode = gamemode
        self.running = True
        self.player = 1  # 1 => cross; 2 => circle

    def draw_board(self) -> None:  # vykresli hru
        screenttt.fill(BG_COLOR)
        pygame.draw.line(screenttt, LINE_COLOR,
                         (SQSIZE, 0), (SQSIZE, HEIGHT), LINE_WIDTH)
        pygame.draw.line(screenttt, LINE_COLOR,
                         (2*SQSIZE, 0), (2*SQSIZE, HEIGHT), LINE_WIDTH)

        pygame.draw.line(screenttt, LINE_COLOR,
                         (0, SQSIZE), (WIDTH, SQSIZE), LINE_WIDTH)
        pygame.draw.line(screenttt, LINE_COLOR,
                         (0, 2*SQSIZE), (WIDTH, 2*SQSIZE), LINE_WIDTH)

    def draw_figure(self, row, col):  # vykresli kolecko nebo krizek
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

    def next_turn(self):  # prepne na dalsi kolo (dalsi hrac)
        self.player = self.player % 2 + 1

    def mark(self, row, col):  # oznaci pole
        self.board.mark_sqr(row, col, self.player)
        self.draw_figure(row, col)
        self.next_turn()

    def isover(self):  # kontrola zda je hra u konce
        return self.board.state(show=True) != 0 or self.board.isfull()

    def ai_turn(self):  # kontrola jestli je na rade ai
        return self.gamemode == "ai" and self.player == self.ai.player


def main():  # hlavni funkce

    game = Game()
    board = game.board
    ai = game.ai
    game.draw_board()
    print(f"AI level : {ai.level}")
    print(f"Gamemod: {game.gamemode}")

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # spoustece na klavesy
            # spusti se pouze po zvednuti, aby se predeslo opakovani spousteni
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_d:  # zmeni uroven ai
                    if not board.running() or board.isempty():
                        ai.level = 0 if ai.level else 1
                        print(f"AI level : {ai.level}")
                    else:
                        print("Can't ai level mid-game")
                if event.key == pygame.K_e:  # zmeni styl hry (pvp, nebo ai)
                    if not board.running() or board.isempty():
                        game.gamemode = "pvp" if game.gamemode == "ai" else "ai"
                        print(f"Gamemode: {game.gamemode}")
                    else:
                        print("Can't set gamemode mid-game")

                if event.key == pygame.K_r:  # resetuje hru
                    game = Game(gamemode=game.gamemode, aistr=ai.level)
                    board = game.board
                    ai = game.ai
                    game.draw_board()
                    print(f"AI level : {ai.level}")
                    print(f"Gamemod: {game.gamemode}")

            # spoustec vykresleni figury (krizek, kolecko)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if (game.gamemode == "ai" and game.player != ai.player) or game.gamemode == "pvp":
                    pos = event.pos
                    row = pos[1] // SQSIZE
                    col = pos[0] // SQSIZE

                    if board.sq_empty(row, col) and board.state() == 0:
                        game.mark(row, col)

                        if game.isover():
                            pygame.display.update()
                            game.running = False
                            if board.state() == 0:
                                pyautogui.alert(
                                    f"Game Over! It's a Tie")
                            else:
                                pyautogui.alert(
                                    f"Game Over! Player {int(board.state())} wins")
        # vykreslovani pomoci ai
        if game.gamemode == "ai" and game.player == ai.player and not board.isfull() and board.state() == 0:
            pygame.display.update()
            row, col = ai.eval(board)
            game.mark(row, col)

            if game.isover():  # kontroluje jestli je hra u konce a oznami vyherce pokud tomu tak je
                pygame.display.update()
                game.running = False
                if board.state() == 0:
                    pyautogui.alert(
                        f"Game Over! It's a Tie")
                else:
                    pyautogui.alert(
                        f"Game Over! Player {int(board.state())} wins")

        pygame.display.update()


main()

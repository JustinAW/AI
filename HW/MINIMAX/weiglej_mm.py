import platform
import time
import random
from math import inf
from os import system

MAX = +1
MIN = -1

board = [
        [0,0,0],
        [0,0,0],
        [0,0,0]]

def check_win (b_state, player):
    winning_board_states = [
        [b_state[0][0], b_state[0][1], b_state[0][2]],
        [b_state[1][0], b_state[1][1], b_state[1][2]],
        [b_state[2][0], b_state[2][1], b_state[2][2]],
        [b_state[0][0], b_state[1][0], b_state[2][0]],
        [b_state[0][1], b_state[1][1], b_state[2][1]],
        [b_state[0][2], b_state[1][2], b_state[2][2]],
        [b_state[0][0], b_state[1][1], b_state[2][2]],
        [b_state[2][0], b_state[1][1], b_state[0][2]],
    ]
    if [player, player, player] in winning_board_states:
        return True
    else:
        return False

def get_empty_cells (b_state):
    empty_cells = []

    for x, row in enumerate(b_state):
        for y, cell in enumerate(row):
            if cell == 0:
                empty_cells.append([x,y])

    return empty_cells


def possible_move (x, y):
    if [x,y] in get_empty_cells(board):
        return True
    else:
        return False


def make_move(x, y, player):
    if (possible_move(x,y)):
        board[x][y] = player
        return True
    else:
        return False


def game_over(b_state):
    return (check_win(b_state, MIN) or check_win(b_state, MAX))


def minimax (b_state, depth, player):
    """ Recursive AI algorithm that minimizes the loss for a move
    params:
        b_state: current state of the game board
        depth: node index in the tree (0 <= depth <= 9)
        player: either min or max player
    returns:
        a list with [best row, best col, best score]
    """
    if depth == 0 or game_over(b_state):
        score = evaluate(b_state)
        return [-1, -1, score]

    if player == MAX:
        best = [-1, -1, -inf]
        for cell in get_empty_cells(b_state):
            x, y = cell[0], cell[1]
            b_state[x][y] = player
            score = minimax(cell, depth - 1, MIN)
            b_state[x][y] = 0
            score[0] = x
            score[1] = y
            if score[2] > best[2]:
                best = score
    elif player == MIN:
        best = [-1, -1, +inf]
        for cell in get_empty_cells(b_state):
            x, y = cell[0], cell[1]
            b_state[x][y] = player
            score = minimax(cell, depth - 1, MAX)
            b_state[x][y] = 0
            score[0] = x
            score[1] = y
            if score[2] < best[2]:
                best = score

    return best


def clear_screen ():
    """
    Clears Console so board can be rendered
    """
    os_name = platform.system().lower()
    if "windows" in os_name:
        system("cls")
    else:
        system("clear")


def main ():
    clear_screen()


if __name__ == "__main__":
    main()

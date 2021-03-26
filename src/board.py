import random
import sys

from cell import *
from src.display_array import display_array


def generate_array(dim=50):
    if (dim<=0):
        print("Dimension must be greater than 0")
        sys.exit()
    arr = [["" for i in range(dim)] for j in range(dim)]

    for i in range(dim):
        for j in range(dim):
            arr[i][j] = cell()
            n = random.randint(1, 100)
            if n>=1 and n<=25:
                arr[i][j].set_terrain("flat")
            elif n>=26 and n<=50:
                arr[i][j].set_terrain("hilly")
            elif n>=51 and n<=75:
                arr[i][j].set_terrain("forest")
            elif n>=75 and n<=100:
                arr[i][j].set_terrain("cave")
            else:
                #default case
                arr[i][j].set_terrain()

    return arr

class board:
    def __init__(self, dim=50):
        self.dim = dim
        self.board = generate_array(dim)

    def get_terrain(self, i, j):
        return self.board[i][j].terrain

    def search_cell(self, i, j):
        return self.board[i][j].search_cell()

    def get_false_negative(self, i, j):
        return self.board[i][j].false_negative

    def isValid(self, row, col):
        if row >= self.dim or row < 0 or col >= self.dim or col < 0:
            return False
        else:
            return True

    def setTarget(self):
        randRow = random.randint(0, self.dim-1)
        randCol = random.randint(0, self.dim-1)
        self.board[randRow][randCol].set_target

    def print_board(self):
        dim = self.dim
        copy = [["" for i in range(dim)] for j in range(dim)]
        for row in range(dim):
            for column in range(dim):
                if self.board[row][column].terrain == 'flat':
                    copy[row][column] = 'FL'
                elif self.board[row][column].terrain == 'hilly':
                    copy[row][column] = 'H'
                elif self.board[row][column].terrain == 'forest':
                    copy[row][column] = 'FR'
                elif self.board[row][column].terrain == 'cave':
                    copy[row][column] = 'C'
                else:
                    copy[row][column] = 'O'

        print("Here is the board")
        for row in copy:
            print(row)

    def display_board(self):
        display_array(self.board, 50)

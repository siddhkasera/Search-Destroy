import random
import sys

from cell import *
from src.display_array import display_array


def generate_array(dim=50):
    """Generates board, and populates it with the terrain types"""
    if (dim <= 0):
        print("Dimension must be greater than 0")
        sys.exit()
    arr = [["" for i in range(dim)] for j in range(dim)]

    for i in range(dim):
        for j in range(dim):
            arr[i][j] = cell()
            n = random.randint(1, 100)
            if n >= 1 and n <= 25:
                arr[i][j].set_terrain("flat")
            elif n >= 26 and n <= 50:
                arr[i][j].set_terrain("hilly")
            elif n >= 51 and n <= 75:
                arr[i][j].set_terrain("forest")
            elif n >= 75 and n <= 100:
                arr[i][j].set_terrain("cave")
            else:
                # default case
                arr[i][j].set_terrain()

    return arr


class board:
    """board class, which stores cell objects"""

    def __init__(self, dim=50):
        self.dim = dim
        self.board = generate_array(dim)

    def get_terrain(self, i, j):
        """
        Gets terrain of the cooresponding cell

        :param i: Row of the cell to be searched
        :param j: Col of the cell to be searched
        :return: String, the terrain type of the cell
        """
        return self.board[i][j].terrain

    def search_cell(self, i, j):
        """
        Checks if the corresponding cell contains the target

        :param i: Row of the cell to be searched
        :param j: Col of the cell to be searched
        :return: boolean, true if found and false otherwise
        """
        return self.board[i][j].search_cell()

    def get_false_negative(self, i, j):
        """
        Check false negative rate of the cell

        :param i:
        :param j:
        :return: Float, the false negative rate of the cell
        """
        return self.board[i][j].false_negative

    def isValid(self, row, col):
        """
        Determine if the cell belongs to the board

        :param row:
        :param col:
        :return: boolean, true if valid, false otherwise
        """
        if row >= self.dim or row < 0 or col >= self.dim or col < 0:
            return False
        else:
            return True

    def randomSetTarget(self, printTarget=False):
        """
        Randomly sets one cell of the board to be target
        See set_target of cell

        :return:
        """
        randRow = random.randint(0, self.dim - 1)
        randCol = random.randint(0, self.dim - 1)
        if printTarget:
            print("The target should be: (" + str(randRow) + ", " + str(randCol) + ")")
        self.board[randRow][randCol].set_target()

    def print_board(self):
        dim = self.dim
        copy = [["" for i in range(dim)] for j in range(dim)]
        targetLocation = (-1, -1)
        row = 0
        col = 0
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
                else:  # other, for some reason
                    copy[row][column] = 'O'

        print("Here is the board")
        for r in copy:
            print(r)
        print("\n")

    def display_board(self):
        display_array(self.board, 50)

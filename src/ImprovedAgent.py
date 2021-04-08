from math import log
from random import randint
from src.AutoAgent import auto_agent, get_manhattan_dist, get_least_manhattan
import board
from src.BasicAgent2 import basic_agent2


class improved_agent(basic_agent2): # TODO
    def __init__(self, b: board, dim=50):
        super().__init__(b, dim)
        self.attemptNo = 1  # Checks number of times I searched a particular cell. Is probably not the best design choice tbh

    # Inherit from basic agent 2
    # Keep confidence state from basic agent 2

    def choose_next_cell(self, row, col, greatest):
        """
        Chooses the next cell to be searched. This time I count the number of times the cell was searched and update doneSearching depending on # of times

        :param row:
        :param col:
        :param greatest: Greatest value of the board
        :return: tuple, of the form (row, col) representing the coordinates
        """

        greatestArr = []
        for nRow in range(self.dim):
            for nCol in range(self.dim):
                if self.kb[nRow][nCol] == greatest:
                    m = get_manhattan_dist(row, col, nRow, nCol)
                    greatestArr.append((nRow, nCol, m))

        # if attemptNo < log(0.01, false neg), then try this cell again; otherwise, move to a new cell
        # It calculates the number of attempts needed to nearly guarantee (99%) that the cell is a target

        if self.attemptNo < log(0.01, self.board.get_false_negative(row, col)):
            self.attemptNo = self.attemptNo + 1
            return (row, col)

        leastDistArr = get_least_manhattan(greatestArr)
        self.attemptNo = 1
        if len(leastDistArr) == 0:
            return (row, col)
        elif len(leastDistArr) == 1:
            self.dist = self.dist + get_manhattan_dist(row, col, leastDistArr[0][0], leastDistArr[0][1])
            return leastDistArr[0]
        else:
            random_elem = randint(0, len(leastDistArr)-1)
            self.dist = self.dist + get_manhattan_dist(row, col, leastDistArr[random_elem][0],
                                                       leastDistArr[random_elem][1])
            return leastDistArr[random_elem]


def exe_improved_agent(b: board, dim=50, printPerformance=False):
    """
    Executes improved agent

    :param b:
    :param dim:
    :param printPerformance: Whether or not I want to print the search results
    :return:
    """
    agent = improved_agent(b, dim)
    return agent.run_agent(printPerformance)

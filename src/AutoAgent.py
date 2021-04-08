from random import randint
import time
import board


def get_manhattan_dist(row1, col1, row2, col2):
    """
    Gets manhattan distance between the two cells

    :param row1:
    :param col1:
    :param row2:
    :param col2:
    :return: int
    """
    distHoriz = abs(row1 - row2)
    distVert = abs(col1 - col2)
    dist = distHoriz + distVert
    return dist


def get_least_manhattan(greatestArr, dim=50):
    """
    From list of tuples, select the one with the least Manhattan distance
    The tuples in greatestArr are of format (row, col, manhattan dist)

    :param greatestArr: List of cells with the greatest probability
    :param dim:
    :return: list, of tuples representing points with the least Manhattan distance. Format is (row, col)
    """
    leastDistArr = []
    current_dist = dim * dim + 1
    for i in greatestArr:
        if i[2] < current_dist:
            current_dist = i[2]
            leastDistArr = [(i[0], i[1])]
        elif i[2] == current_dist:
            leastDistArr.append((i[0], i[1]))

    return leastDistArr


#######################################################################################################

class auto_agent:
    """
    Class that serves as an "interface" for the automated agents (Python lacks native interface support)

    I recommend overriding update_kb with the appropriate formulas
    """

    def __init__(self, b: board, dim=50):
        self.board = b
        self.dim = dim
        self.kb = [[1 / dim for i in range(dim)] for j in range(dim)]
        self.dist = 0
        self.time = 0

    def run_agent(self, printPerformance=False):
        start = time.time()
        row = randint(0, self.dim-1)
        col = randint(0, self.dim-1)
        while True:
            self.time = self.time + 1
            result = self.board.search_cell(row, col)
            if result:
                break
            else:  # target NOT found
                self.update_kb(row, col, self.board.get_false_negative(row, col))
                greatest = self.get_greatest_probability()
                next_coords = self.choose_next_cell(row, col, greatest)
                row = next_coords[0]
                col = next_coords[1]
        end = time.time()
        if printPerformance:
            print("RESULTS:")
            print("Target located at: (" + str(row) + ", " + str(col) + ")")
            print("Terrain type was: " + self.board.board[row][col].terrain)
            print(str(self.time) + " iterations")
            print(str(self.dist) + " distance")
            print(str(self.time + self.dist) + " total score")
            print(str(end-start) + " seconds")

        return self.time + self.dist  # The total score

    def search_cell(self, row, col):
        """
        Search the given cell. Also would call update_kb and update kn based off of the results

        :param row: Current row coord
        :param col: Current col coord
        :return: boolean, true if found, false otherwise
        """
        isFound = self.board.search_cell(row, col)

        if isFound:
            return True

        return False

    def get_greatest_probability(self):
        """
        Gets the greatest value of the kb

        :return: float
        """
        greatest = -1
        for i in range(self.dim):
            for j in range(self.dim):
                if self.kb[i][j] > greatest:
                    greatest = self.kb[i][j]

        return greatest

    def update_kb(self, row, col, falseNeg, result: bool = False):
        """
        I recommend overriding this one with the formula used to calculate the knowledge and belief states

        :param row:
        :param col:
        :param falseNeg: the false negative rate of the cell
        :param result: bool, the results of the search (should be false)
        :return:
        """
        pass

    def choose_next_cell(self, row, col, greatest):
        """
        Chooses the next cell to be searched. May be overridden in case the advanced agent has a different approach to selecting the next cell

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

        leastDistArr = get_least_manhattan(greatestArr)
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

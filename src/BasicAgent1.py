from src.AutoAgent import auto_agent
import board


class basic_agent1(auto_agent):
    def __init__(self, b: board, dim=50):
        super().__init__(b, dim)

    # Override
    def update_kb(self, row, col, falseNeg, result: bool = False):
        """
        Overrides update_kb of auto_agent
        Calculates the belief state
        """
        # self.dim = dim
        # self.kb = [[1 / dim for i in range(dim)] for j in range(dim)] -- when time equals 0

        on_opening = falseNeg * self.kb[row][col]  # will start at falseNeg * 1/dim*dim
        before_opening = 1  # Certain that I will select this exact cell
        remaining_prob = 0
        for r in range(self.dim):
            for c in range(self.dim):
                if r != row or c != col:
                    remaining_prob = remaining_prob + self.kb[r][c]

        after_opening = (before_opening * on_opening) + remaining_prob

        self.kb[row][col] = on_opening

        # normalize here
        for r in range(self.dim):
            for c in range(self.dim):
                self.kb[r][c] = self.kb[r][c] / after_opening

        return


def exe_basic_agent1(b: board, dim=50, printPerformance=False):
    """
    Executes basic agent 1

    :param b:
    :param dim:
    :param printPerformance: Whether or not I want to print the search results
    :return:
    """
    agent = basic_agent1(b, dim)
    agent.run_agent(printPerformance)

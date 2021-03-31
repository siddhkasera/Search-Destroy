from src.AutoAgent import auto_agent
import board


class basic_agent2(auto_agent):
    def __init__(self, b: board, dim=50):
        super().__init__(b, dim)

    # Override
    def update_kb(self, row, col, falseNeg, result: bool): # TODO: calculate and update CONFIDENCE states
        """
        Overrides update_kb of auto_agent
        Should calculate confidence state
        """
        pass


def exe_basic_agent2(b: board, dim=50, printPerformance=False):
    """
    Executes basic agent 2

    :param b:
    :param dim:
    :param printPerformance: Whether or not I want to print the search results
    :return:
    """
    agent = basic_agent2(b, dim)
    agent.run_agent(printPerformance)

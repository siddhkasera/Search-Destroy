import sys
from functools import reduce

import matplotlib.pyplot as plt
from board import *
from src.BasicAgent1 import exe_basic_agent1
from src.BasicAgent2 import exe_basic_agent2
from src.ImprovedAgent import exe_improved_agent


def avg(list):
    sum = 0
    sum += reduce(lambda a, b: a + b, list)
    avg = sum / len(list)
    return avg


def automate_test():
    print("AUTOMATED TESTING SCRIPT")
    num_tests = input("How many attempts do you want to run (min recommended is 10)? ")
    file_name = input("Input the name of the file you want to store the raw output, and remember extensions:\n")
    print("Starting tests...")
    results1 = []
    results2 = []
    resultsIm = []

    orig_stdout = sys.stdout
    f = open(file_name, "w")
    sys.stdout = f
    print("AUTOMATED TEST RESULT DATA")
    print("Credits: Siddhi Kasera and Em Shi")
    print(num_tests + " attempts per agent")
    print("----------------------------")
    a = 0
    while a < int(num_tests):
        board1 = board(50)
        res1 = exe_basic_agent1(board1, board1.dim, True)

        board2 = board(50)
        res2 = exe_basic_agent2(board2, board2.dim, True)

        boardIm = board(50)
        resIm = exe_improved_agent(boardIm, boardIm.dim, True)

        results1.append(res1)
        results2.append(res2)
        resultsIm.append(resIm)

        del board1, board2, boardIm, res1, res2, resIm

        a = a+1

    print(results1)
    print(results2)
    print(resultsIm)

    print("End of raw data")
    print("\nHere are the avg scores:")
    print("Basic agent 1: ", str(avg(results1)))
    print("Basic agent 2: ", str(avg(results2)))
    print("Improved agent: ", str(avg(resultsIm)))

    sys.stdout = orig_stdout
    f.close()

    print("\nTerminating the program")

    sys.exit()

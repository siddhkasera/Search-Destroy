from board import *
from ManualAgent import *
from src.BasicAgent1 import exe_basic_agent1
from src.BasicAgent2 import exe_basic_agent2

agent = input("Which agent do you want to use? ")

board = board(50)
#board.display_board()

printTarget = input("Would you like to see what the actual target should be? Y/N ")
p = False
if printTarget == "Y" or printTarget == "y" or printTarget == "yes" or printTarget == "Yes":
    p = True
else:
    p = False
board.randomSetTarget(p)

#board.print_board()

if agent == 'manual' or agent == 'Manual' or agent == 'm' or agent == "M":
    manual_agent(board)

elif agent == "Basic 1" or agent == "basic 1" or agent == "b1" or agent == "B1":
    print("Running basic agent 1...\n")
    exe_basic_agent1(board, 50, True)

elif agent == "Basic 2" or agent == "basic 2" or agent == "b2" or agent == "B2":
    print("Basic agent 2 not implemented")
    # TODO: exe_basic_agent2(board, 50)

elif agent == "improved" or agent == "Improved" or agent == "I" or agent == "i" or agent == "Advanced" or agent == "advanced":
    print("Improved agent not implemented")

else:
    print("That's not an agent!")

print("Terminating the program")
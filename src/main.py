from board import *
from ManualAgent import *


agent = input("Which agent do you want to use? ")

board = board(50)
#board.print_board()
#board.display_board()

if agent == 'manual' or agent == 'Manual' or agent == 'm' or agent == "M":
    manual_agent(board)

elif agent == "Basic 1" or agent == "basic 1" or agent == "b1" or agent == "B1":
    print("Basic agent 1 not implemented")

elif agent == "Basic 2" or agent == "basic 2" or agent == "b2" or agent == "B2":
    print("Basic agent 2 not implemented")

elif agent == "improved" or agent == "Improved" or agent == "I" or agent == "i" or agent == "Advanced" or agent == "advanced":
    print("Improved agent not implemented")

else:
    print("That's not an agent!")
from board import *
from ManualAgent import *
from BasicAgent1 import exe_basic_agent1
from BasicAgent2 import exe_basic_agent2
from ImprovedAgent import exe_improved_agent
from auto_test import automate_test
auto = input("Would you like to automate testing? Y/N ")
if auto == "Y" or auto == "y" or auto == "Yes" or auto == "yes":
    automate_test()

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
res = 0

output = input("Would you like to redirect the output to a file? Y/N ")
if output == "Y" or output == "y" or output == "Yes" or output == "yes":
    file_name = input("What is the name of the file you want to output to? Remember file extensions! ")
    print("Redirecting output to the file...")
    orig_stdout = sys.stdout
    f = open(file_name, "w")
    sys.stdout = f
    print("Agent: " + agent)

if agent == 'manual' or agent == 'Manual' or agent == 'm' or agent == "M":
    manual_agent(board)

elif agent == "Basic 1" or agent == "basic 1" or agent == "b1" or agent == "B1":
    print("Running basic agent 1...\n")
    res = exe_basic_agent1(board, 50, True)

elif agent == "Basic 2" or agent == "basic 2" or agent == "b2" or agent == "B2":
    print("Running basic agent 2...\n")
    res = exe_basic_agent2(board, 50, True)

elif agent == "improved" or agent == "Improved" or agent == "I" or agent == "i" or agent == "Advanced" or agent == "advanced":
    print("Running improved agent...\n")
    res = exe_improved_agent(board, 50, True)

else:
    print("That's not an agent!")

if output == "Y" or output == "y" or output == "Yes" or output == "yes":
    sys.stdout = orig_stdout
    f.close()

print("\nTerminating the program")
from board import *


def manual_agent(b: board, dim=50):
    isFound = False
    hasDropped = False
    row = -1
    col = -1


    print("This is the manual agent")
    print("----------------------------\n")

    while not isFound:
        print("\nHere are the options:")
        print("1: Search a cell")
        print("2: Print the field")
        print("3: Get coords of cell last searched")
        print("Q: Quit")
        option = input("Select option: ")
        if option == "1" or option == "search" or option == "Search":
            row = input("Select a row, must be from a range of 0 to " + str(b.dim - 1) + ": ")
            col = input("Select a col, must be from a range of 0 to " + str(b.dim - 1) + ": ")
            while not b.isValid(int(row), int(col)):
                print("Invalid coords, please try again.")
                row = input("Select a row, must be from a range of 0 to " + str(b.dim - 1) + ": ")
                col = input("Select a col, must be from a range of 0 to " + str(b.dim - 1) + ": ")
            hasDropped = True
            isFound = b.search_cell(int(row), int(col) )
            if isFound:
                print("Target located")
            else:
                print("Target not located")
                print("False negative rate was " + str(b.get_false_negative(int(row), int(col))))

        elif option == "2" or option == "Print" or option == "print":
            b.print_board()

        elif option == "3":
            if hasDropped:
                print("Here were the coordinates from last time: (" + row + ", " + col+ ")")
            else:
                print("Nothing selected from last time")

        elif option == 'Q' or option == "Quit" or option == 'quit':
            print("Quit")
            break

        else:
            print("Invalid option")

    return 0

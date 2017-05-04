from classes import * #importing classes
b = Board()
p1 = Player('yellow', b)
p2 = Player('red', b)

ill = Illustrator(b)
#gameWon = True
def mainMenu():
    print("Welcome to Connect4.py!")
    print("written by Jeffrey 'wroje' Wrobel")
    print("1. Play!\n2. About")
    mainMenuInput = input()
    if mainMenuInput == '1':
        gameWon == False
    elif mainMenuInput == '2':
        print("This program was written for KJHS 2nd Semester CompSci")
        print()
        print("License: Free for all personal use and modification.\nNo commercial use. \nAttribute 'Jeffrey Wrobel' when using this code. ")
        print("Credits:\nProgramming: Jeffrey Wrobel\nOriginal Game: Howard Wexler, Ned Strongin,\nSpecial Thanks To: \nMr. Daniel Kelley")
        print("Connect4 is property of Hasbro Inc. ")
        print()
        print("clone the source code!")
        print("https://github.com/WroJe/connect4-py.git")
        print()
        print("Press any key to continue...")
        menuReStart = input()
        mainMenu()
    else:
        print("err")

mainMenu()
while gameWon == False:
    ill.draw()
    p1.take_turn()
    b.check_win()
    ill.draw()
    p2.take_turn()
    b.check_win()

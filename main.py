from classes import * #importing classes
b = Board()
p1 = Player('yellow', b)
p2 = Player('red', b)

ill = Illustrator(b)

def mainMenu(self):
    print("Welcome to Connect4.py!")
    print("written by Jeffrey 'wroje' Wrobel")
    mainMenuInput = input(print("1. Play! \n 2. About"))
        if mainMenuInput = 1:
            gameWon = False
        elif mainMenuInput = 2:
            print("This program was written for KJHS 2nd Semester CompSci")
            print()
            print("License: Free for all personal use and modification.\n No commercial use. \n Attribute 'Jeffrey Wrobel' when using this code. ")
            print("Credits \n Programming: Jeffrey Wrobel \n  Original Game: Howard Wexler, Ned Strongin,\n Special Thanks To: \n Mr. Daniel Kelley")
            print("Connect4 is property of Hasbro Inc. ")
            print()
            print("clone the source code!")
            print("https://github.com/WroJe/connect4-py.git")
            print()
            input(print("Press any key to continue...."))
        else:
            print("err")

while gameWon = False:
    ill.draw()
    p1.take_turn()
    b.check_win()
    ill.draw()
    p2.take_turn()
    b.check_win()

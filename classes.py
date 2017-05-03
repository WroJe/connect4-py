import random

gameWon = False

class Board:
    """
    responsibilities:
    * Retain Piece info
    * Tracking Red and Yellow piece positions
    * Board is 6 columns 7 rows
    """
    def __init__(self):
        # self.boardColumns = 6
        self.boardRows = 7
        self.pieces = {
            'a': [],
            'b': [],
            'c': [],
            'd': [],
            'f': [],
            'g': []
        }

        # self.pos {
        #     'xpos': ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
        #     'ypos': [ 1, 2, 3, 4, 5, 6],
        #     }

    def drop(self):
        pass

    def play(self, column, piece):
        if len(self.board[column]) == self.boardRows: #checking to see if the column is full
            return False
        self.board[column].append(piece)
            return True

class Piece:
    """  """
    def __init__(self, color):
        self.color = color


class Player:

    def __init__(self, color, board):
        self.color = color
        self.board = board

    def take_turn(self):
        """
        Taking player input on which column they wish to put their piece in
        Appending the list of that input, and  returning an error if it doesn't exist
        """
        choice = input('Which column do you wish to drop your piece in? \n a, b, c, d, e, f, or g?')
        if self.board.play(choice):
            return
        else:
            print("You can't go there")
            return self.take_turn()

class Illustrator:
    def __init__(self, board):
        pass

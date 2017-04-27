import random

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
        if len(self.board[column]) == self.boardRows:
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
        choice = input('Which column do  you choose?')

        if self.board.play(choice):
            return
        else:
            print('Youo cant go there')
            return self.take_turn()

class Menu:
    def __init__(sels):
        user-place = 0

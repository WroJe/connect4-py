import random

class Board:
    """
    responsibilities:
    * Drawing game Board
    * Retain Piece info
    * Tracking Red and Yellow piece positions
    * Board is 6 columns 7 rows
    """
    def __init__(self):
        self.boardColumns = 6
        self.boardRows = 7
        self.positions = {x: ['A', 'B', 'C', 'D', 'E', 'F', 'G'], y: [ 1, 2, 3, 4, 5, 6]}

    def drop(self, xAxis):


class Piece:
    """  """
    def __init__(self):
        self.pos = [][]

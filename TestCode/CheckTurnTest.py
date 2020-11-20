import unittest

from Main.py import *

class CheckTurnTest(unittest.TestCase):
    def CheckTurnTest (self, turn, color):
        for player_turn in range(101):
                if (turn % 2 == 0):
                    
                    # assert Player = Player A
                    self.assert COLOR == BLACK #Color here is a local vaiable, same with turn
                else:
                    
                    # assert Player = Player B
                    self.assert COLOR == WHITE
                

import unittest

from Main.py import *

class CheckTurnTest(unittest.TestCase):
    def CheckTurnTest (self, turn, COLOR):
        for player_turn in range(101):
                if (turn % 2 == 0):
                    # assert Player = Player A
                    self.assertEqual(COLOR) == BLACK #Color here is a local vaiable, same with turn
                else:
                    # assert Player = Player B
                    self.assertEqual(COLOR) == WHITE
                
if __name__ == '__main__': 
    unittest.main() 
                

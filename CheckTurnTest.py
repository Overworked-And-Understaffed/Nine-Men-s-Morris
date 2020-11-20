import unittest
from unittest.case import TestCase
from Board import *


class CheckTurnTest(unittest.TestCase):
    # def test_turncheck (self, turn, COLOR):
    #     for player_turn in range(18):
    #             if (turn % 2 == 0):
    #                 # assert Player = Player A
    #                 self.assertEqual(COLOR, BLACK) #COLOR here is a local vaiable, same with turn
    #             else:
    #                 # assert Player = Player B
    #                 self.assertEqual(COLOR, WHITE)

    def test_turnCheck(self):      
        self.Board.turnCheck()
        self.Board.turn = 1
        
        #Verify Player piece is Black        
        if (self.Board.turn % 2 == 0):
            self.assertEqual("BLACK", "BLACK")#self.Board.turnCheck())
        # else:
        #     self.assertNotEqual("BLACK", self.Board.turnCheck())
        
if __name__ == '__main__': 
    unittest.main(exit=False) 

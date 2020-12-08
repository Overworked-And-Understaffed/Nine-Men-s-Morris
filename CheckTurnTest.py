import unittest
import pygame
import os
import sys
from pygame.locals import *
import Board

from Globals import *

class CheckTurnTest(unittest.TestCase):
    def test_CheckTurnTest(self):
        pygame.init()
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        board = Board.Board(screen)
        for playerTurn in range(101):
            board.turn = playerTurn
            if (playerTurn % 2 == 0):
                # assert Player = Player A
                self.assertEqual(board.turnCheck(),"BLACK")
            else:
                # assert Player = Player B
                self.assertEqual(board.turnCheck(),"WHITE")
        print("End")
        return 
                

  """   def testTurnCheck(self):      
        self.Board.turnCheck()
        self.Board.turn = 1
        
        #Verify Player piece is Black        
        if (self.Board.turn % 2 == 0):
            self.assertEqual("BLACK", "BLACK")#self.Board.turnCheck())
        # else:
        #     self.assertNotEqual("BLACK", self.Board.turnCheck()) """
        
if __name__ == '__main__': 
    unittest.main(exit=False) 

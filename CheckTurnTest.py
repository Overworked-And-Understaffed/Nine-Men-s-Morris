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
        for player_turn in range(101):
            board.turn = player_turn
            if (player_turn % 2 == 0):
                # assert Player = Player A
                self.assertEqual(board.turnCheck(),"BLACK")
            else:
                # assert Player = Player B
                self.assertEqual(board.turnCheck(),"WHITE")
        print("End")
        return 
                
if __name__ == '__main__': 
    unittest.main() 
                
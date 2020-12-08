import unittest
import pygame
import os
import sys
from pygame.locals import *
import Board

from Globals import *
from GameLogic import cordsToNum

class PieceLocationTest(unittest.TestCase):
    def testPieceLocationTest(self):
        pygame.init()
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        board = Board.Board(screen)
        xyRange = 25

        for x in range(800):
            for y in range(800):
                for i in board.boardCoords:
                    if i[0] > x - xyRange and i[0] < x + xyRange and i[1] > y - xyRange and i[1] < y + xyRange :
                        assert self.Piece_Location(x, y, board.boardCoords)# == True, ("Issue at", x, y)
                    else:
                        assert self.Piece_Location(x, y, board.boardCoords)# == False, ("Issue at", x, y)

if __name__ == '__main__':
    unittest.main(exit=False)

import pygame
import os
import sys
import random
from pygame.locals import *
import unittest

from Globals import *
import Board
import AIHeuristic
import GameLogic

class ComputerTest(unittest.TestCase):
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    board = Board.Board(screen)
    #If it is Phase 1 and there is the opportunity for the computer to make a mill, it will
    def testMakeMillPhase1Test(self):
        self.takenSpots = ['Insert values here']
        self.whitePlaced = ['Insert values here']
        self.blackPlaced = ['Insert values here']
        self.pieceLocation = AIHeuristic.AIPhase1(self.takenSpots, self.whitePlaced, self.blackPlaced)
        #assert self.pieceLocation = ADD PIECE THAT IT SHOULD MOVE TO HERE
    #If it is Phase 2 and there is the opportunity for the computer to make a mill, it will
    def testMakeMillPhase2Test(self):
        self.takenSpots = ['Insert values here']
        self.whitePlaced = ['Insert values here']
        self.blackPlaced = ['Insert values here']
    #If it is Phase 3 and there is the opportunity for the computer to make a mill, it will
    def testMakeMillPhase3Test(self):
        self.takenSpots = ['Insert values here']
        self.whitePlaced = ['Insert values here']
        self.blackPlaced = ['Insert values here']
    #If it is Phase 1 and there is the opportunity for the computer to block a mill, it will
    def testBlockMillPhase1Test(self):
        self.takenSpots = ['Insert values here']
        self.whitePlaced = ['Insert values here']
        self.blackPlaced = ['Insert values here']
        self.pieceLocation = AIHeuristic.AIPhase1(self.takenSpots, self.whitePlaced, self.blackPlaced)
        #assert self.pieceLocation = ADD PIECE THAT IT SHOULD MOVE TO HERE
    #If it is Phase 2 and there is the opportunity for the computer to block a mill, it will
    def testBlockMillPhase2Test(self):
        self.takenSpots = ['Insert values here']
        self.whitePlaced = ['Insert values here']
        self.blackPlaced = ['Insert values here']
    #If it is Phase 3 and there is the opportunity for the computer to block a mill, it will
    def testBlockMillPhase3Test(self):
        self.takenSpots = ['Insert values here']
        self.whitePlaced = ['Insert values here']
        self.blackPlaced = ['Insert values here']

#OTHER TESTS: Black will place (Phase 1) an adjacent piece (use an or statement to assert that it's either going to place a piece down in one location or the other)
    
if __name__ == '__main__': 
    unittest.main() 

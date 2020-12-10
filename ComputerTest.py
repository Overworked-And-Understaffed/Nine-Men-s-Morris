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
        self.takenSpots = [0,6,9,13,18]
        self.whitePlaced = [6,13,18]
        self.blackPlaced = [0,9]
        self.pieceLocation = AIHeuristic.AIPhase1(self.takenSpots, self.whitePlaced, self.blackPlaced)
        assert self.pieceLocation == 21
    #If it is Phase 2 and there is the opportunity for the computer to make a mill, it will
    def testMakeMillPhase2Test(self):
        self.takenSpots = [0,6,9,13,14,18,22]
        self.whitePlaced = [6,13,18]
        self.blackPlaced = [0,9,14,22]
        self.stored, self.pieceLocation = AIHeuristic.AIphase2(self.takenSpots, self.whitePlaced, self.blackPlaced)
        assert self.pieceLocation == 21
    #If it is Phase 3 and there is the opportunity for the computer to make a mill, it will
    def testMakeMillPhase3Test(self):
        self.takenSpots = [0,6,9,11,13,18]
        self.whitePlaced = [6,13,18]
        self.blackPlaced = [0,9,11]
        self.stored, self.pieceLocation = AIHeuristic.AIFlying(self.takenSpots, self.whitePlaced, self.blackPlaced)
        assert self.pieceLocation == 21
    #If it is Phase 1 and there is the opportunity for the computer to block a mill, it will
    def testBlockMillPhase1Test(self):
        self.takenSpots = [0,6,9,13,18]
        self.whitePlaced = [0,9,18]
        self.blackPlaced = [6,13]
        self.pieceLocation = AIHeuristic.AIPhase1(self.takenSpots, self.whitePlaced, self.blackPlaced)
        assert self.pieceLocation == 21
    #If it is Phase 2 and there is the opportunity for the computer to block a mill, it will
    def testBlockMillPhase2Test(self):
        self.takenSpots = [0,6,9,13,14,18,22]
        self.whitePlaced = [0,9,14,18]
        self.blackPlaced = [6,13,22]
        self.stored, self.pieceLocation = AIHeuristic.AIphase2(self.takenSpots, self.whitePlaced, self.blackPlaced)
        assert self.pieceLocation == 21
    #If it is Phase 3 and there is the opportunity for the computer to block a mill, it will
    def testBlockMillPhase3Test(self):
        self.takenSpots = [0,6,9,11,13,18]
        self.whitePlaced = [0,9,11]
        self.blackPlaced = [6,13,18]
        self.stored, self.pieceLocation = AIHeuristic.AIFlying(self.takenSpots, self.whitePlaced, self.blackPlaced)
        assert self.pieceLocation == 21
    #If it is Phase 1 and there are no mills to block/create, it will place a piece adjacent to an existing piece it owns
    def testAdjPhase1Test(self):
        self.takenSpots = [0,6,7,8,11,12,16]
        self.whitePlaced = [0,7,11,12]
        self.blackPlaced = [6,8,16]
        self.pieceLocation = AIHeuristic.AIPhase1(self.takenSpots, self.whitePlaced, self.blackPlaced)
        assert (self.pieceLocation == 15 or self.pieceLocation == 17)
    #If it is Phase 2 and there are no mills to block/create, it will move a piece adjacent to an existing piece it owns
    def testAdjPhase2Test(self):
        self.takenSpots = [6,7,11,12,16,18,20]
        self.whitePlaced = [7,11,12,16]
        self.blackPlaced = [6,18,20]
        self.stored, self.pieceLocation = AIHeuristic.AIphase2(self.takenSpots, self.whitePlaced, self.blackPlaced)
        assert self.pieceLocation == 19
    #If it is Phase 3 and there are no mills to block/create, it will move a piece adjacent to an existing piece it owns
    def testAdjPhase3Test(self):
        self.takenSpots = [6,7,8,11,12,16]
        self.whitePlaced = [7,11,12]
        self.blackPlaced = [6,8,16]
        self.stored, self.pieceLocation = AIHeuristic.AIFlying(self.takenSpots, self.whitePlaced, self.blackPlaced)
        assert (self.pieceLocation == 15 or self.pieceLocation == 17)
    #If it is Phase 1 and there are no mills to block/create, or places to put adjacent pieces 
    #It will place a piece at random
    def testRandomPhase1Test(self):
        self.takenSpots = [6,7,8,11,12,16,17]
        self.whitePlaced = [7,11,12,16]
        self.blackPlaced = [6,8,17]
        self.pieceLocation = AIHeuristic.AIPhase1(self.takenSpots, self.whitePlaced, self.blackPlaced)
        self.blackPlaced.append(self.pieceLocation)
        assert len(self.blackPlaced) == 4
    #If it is Phase 2 and there are no mills to block/create, or places to move adjacent pieces 
    #It will move a piece at random
    def testRandomPhase2Test(self):
        self.takenSpots = [6,7,8,11,12,16,17,19]
        self.whitePlaced = [7,11,12,16]
        self.blackPlaced = [6,8,17,19]
        self.stored, self.pieceLocation = AIHeuristic.AIphase2(self.takenSpots, self.whitePlaced, self.blackPlaced)
        assert (self.pieceLocation == 18 or self.pieceLocation == 20)
    #If it is Phase 3 and there are no mills to block/create, or places to move adjacent pieces 
    #It will move a piece at random
    def testRandomPhase3Test(self):
        self.takenSpots = [6,7,8,11,12,16,17]
        self.whitePlaced = [7,11,12,16]
        self.blackPlaced = [6,8,17]
        self.stored, self.pieceLocation = AIHeuristic.AIFlying(self.takenSpots, self.whitePlaced, self.blackPlaced)
        self.blackPlaced.append(self.pieceLocation)
        self.blackPlaced.remove(self.stored)
        assert self.blackPlaced != [6,8,17]
    #If it is Phase 1 and the first piece is being placed, it will be placed at random
    def testPlaceRandomFirstPiece(self):
        self.takenSpots = [6]
        self.whitePlaced = [6]
        self.blackPlaced = []
        self.pieceLocation = AIHeuristic.AIPhase1(self.takenSpots, self.whitePlaced, self.blackPlaced)
        self.blackPlaced.append(self.pieceLocation)
        assert len(self.blackPlaced) == 1

if __name__ == '__main__': 
    unittest.main() 

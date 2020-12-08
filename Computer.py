import pygame
import os
import sys
import random
from pygame.locals import *

from Board import *
import GameLogic

class Computer:
    def __init__(self, phase, takenSpots, whitePlaced, blackPlaced):
        self.phase = phase
        self.takenSpots = takenSpots
        self.whitePlaced = whitePlaced
        self.blackPlaced = blackPlaced

    def ComputerTurn(self):
        if phase == 1:
            #ADD CODE HERE
            print()
import pygame
from Main.py import *

def CheckTurnTest (turn):
   for i in range(101):
        if (turn % 2 == 0):
            # assert Player = Player A
            assert COLOR == BLACK
        else:
            # assert Player = Player B
            assert COLOR == WHITE
        

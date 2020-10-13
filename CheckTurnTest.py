import pygame
from Main.py import *

def CheckTurnTest (turn, color):
   for i in range(101):
        if (turn % 2 == 0):
            # assert Player = Player A
            assert COLOR == BLACK #Color here is a local vaiable, same with turn
        else:
            # assert Player = Player B
            assert COLOR == WHITE
        
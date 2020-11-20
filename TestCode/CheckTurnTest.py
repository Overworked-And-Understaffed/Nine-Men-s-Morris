import pygame
import sys

sys.path.insert(1, '/path/to/Nine-Men-s-Morris') 

import Main.py


def CheckTurnTest (turn, color):
   for i in range(101):
        if (turn % 2 == 0):
            # assert Player = Player A
            assert COLOR == BLACK #Color here is a local vaiable, same with turn
        else:
            # assert Player = Player B
            assert COLOR == WHITE
        
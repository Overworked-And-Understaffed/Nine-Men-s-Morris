""" import pygame
import os
import sys
from pygame.locals import *

from Globals import *
import Menu
import Board
import GameLogic

def CheckWinnerTestWhite ():
    board = Board.Board(screen)
    menu = Menu.Menu(board)
    board.winner = "WHITE"
    menu.winner = "WHITE"
    assert board.winner == menu.winner

def CheckWinnerTestBlack ():
    board = Board.Board(screen)
    menu = Menu.Menu(board)
    board.winner = "BLACK"
    menu.winner = "BLACK"
    assert board.winner == menu.winner """
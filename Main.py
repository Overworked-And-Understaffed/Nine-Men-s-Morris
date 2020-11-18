import pygame
import os
import sys
from pygame.locals import *

from Globals import *
import Menu
import Board
import GameLogic

pygame.init()

# Setup Screen
#-------------------------------------------------
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Nine Men's Morris")

clock = pygame.time.Clock()

board = Board.Board(screen)
menu = Menu.Menu(board)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousePosition = pygame.mouse.get_pos()
            if menu.isMenu:
                menu.handleMenuClick(screen, mousePosition)
                board.clearBoard()
            elif board.handleMouseClick(mousePosition[0], mousePosition[1]):
                menu.isMenu = True
                menu.isEndScreen = True
                menu.winner = board.winner
        
    if menu.isMenu:
        menu.drawMenu(screen)
      
    clock.tick(FPS)
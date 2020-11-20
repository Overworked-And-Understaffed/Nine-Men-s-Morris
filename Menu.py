from Globals import *
import Board

import pygame, sys
from pygame.locals import *

class Menu:
    def __init__(self, board):
      self.isMenu = True
      self.isInstructions = False
      self.isEndScreen = False
      self.winner = ""
      self.board = board
      
      # Initialize Fonts
      self.instructionsFont = pygame.font.SysFont(None, 25)
      self.menuFont = pygame.font.SysFont(None, 30)
      self.largeFont = pygame.font.SysFont(None, 60)
    
      # Button Coordinates, Size and Text
      #-------------------------------------------------
      self.pvpTxt = self.menuFont.render("Player vs Player", True, YELLOW)
      self.pveTxt = self.menuFont.render("Player vs Computer", True, YELLOW)
      self.insTxt = self.menuFont.render("Instructions", True, YELLOW)
      self.exitTxt = self.menuFont.render("Quit", True, YELLOW)
      self.backTxt = self.menuFont.render("Back", True, YELLOW)

      self.pvpTxtHgl = self.menuFont.render("Player vs Player", True, BLACK)
      self.pveTxtHgl = self.menuFont.render("Player vs Computer", True, BLACK)
      self.insTxtHgl = self.menuFont.render("Instructions", True, BLACK)
      self.exitTxtHgl = self.menuFont.render("Quit", True, BLACK)
      self.backTxtHgl = self.menuFont.render("Back", True, BLACK)

      self.pvpSize = self.menuFont.size("Player vs Player")
      self.pvpRect = Rect((int(WIDTH * 0.5) - int(self.pvpSize[0] / 2),
                  int(HEIGHT * 0.4) - int(self.pvpSize[1] / 2)), self.pvpSize)

      self.pveSize = self.menuFont.size("Player vs Computer")
      self.pveRect = Rect((int(WIDTH * 0.5) - int(self.pveSize[0] / 2),
                  int(HEIGHT * 0.5) - int(self.pveSize[1] / 2)), self.pveSize)

      self.insSize = self.menuFont.size("Instructions")
      self.insRect = Rect((int(WIDTH * 0.5) - int(self.insSize[0] / 2),
                  int(HEIGHT * 0.6) - int(self.insSize[1] / 2)), self.insSize)

      self.exitSize = self.menuFont.size("Quit")
      self.exitRect = Rect((int(WIDTH * 0.5) - int(self.exitSize[0] / 2),
                  int(HEIGHT * 0.7) - int(self.exitSize[1] / 2)), self.exitSize)

      self.backSize = self.menuFont.size("Back")
      self.backRect = Rect((int(WIDTH * 0.5) - int(self.backSize[0] / 2),
                  int(HEIGHT * 0.7) - int(self.backSize[1] / 2)), self.backSize)
      
    def drawMenu(self, screen):
      screen.fill(GRAY)
      mousePos = pygame.mouse.get_pos()
      if self.isInstructions:
        heading = self.largeFont.render("Instructions", True, YELLOW)
        headingSize = self.largeFont.size("Instructions")
        headingPos = (int(WIDTH * 0.5) - int(headingSize[0] / 2),
                           int(HEIGHT * 0.2) - int(headingSize[1] / 2))
        screen.blit(heading, headingPos)

        self.drawInstruction(
            "This is an abstract stategy board game with 2 players.",
            0.3, screen)
        self.drawInstruction(
            "Each player has 9 pieces, taking turns placing.",
            0.35, screen)
        self.drawInstruction(
            "The goal is to get your opponent down to 2 pieces only.",
            0.4, screen)
        self.drawInstruction(
            "To accomplish this...",
            0.45, screen)
        self.drawInstruction(
            "Get 3 of your pieces on one line to create a 'mill'.",
            0.5, screen)
        self.drawInstruction(
            "Once you create a mill, you can then remove",
            0.55, screen)
        self.drawInstruction(
            "one of your opponent's pieces from the board. ",
            0.6, screen)
        
        if(self.backRect.collidepoint(mousePos)):
            screen.blit(self.backTxtHgl, (self.backRect.x, self.backRect.y))
        else:
            screen.blit(self.backTxt, (self.backRect.x, self.backRect.y))
      elif self.isEndScreen:
        if self.winner == "WHITE":
            heading = self.largeFont.render("WHITE Player Wins!", True, YELLOW)
            headingSize = self.largeFont.size("WHITE Player Wins!")
            headingPos = (int(WIDTH * 0.5) - int(headingSize[0] / 2), int(HEIGHT * 0.2) - int(headingSize[1] / 2))
            screen.blit(heading, headingPos)
            #Manual Test 13.1
            #print("White Win Menu printed")
        if self.winner == "BLACK":
            heading = self.largeFont.render("BLACK Player Wins!", True, YELLOW)
            headingSize = self.largeFont.size("BLACK Player Wins!")
            headingPos = (int(WIDTH * 0.5) - int(headingSize[0] / 2), int(HEIGHT * 0.2) - int(headingSize[1] / 2))
            screen.blit(heading, headingPos)
            #Manual Test 13.2
            #print("White Win Menu printed")

        self.replayTxt = self.menuFont.render("Play Again", True, YELLOW)
        self.closeTxt = self.menuFont.render("Close", True, YELLOW)
        
        self.replayTxtHgl = self.menuFont.render("Play Again", True, BLACK)
        self.closeTxtHgl = self.menuFont.render("Close", True, BLACK)
        
        self.replaySize = self.menuFont.size("Play Again")
        self.replayRect = Rect((int(WIDTH * 0.5) - int(self.replaySize[0] / 2), int(HEIGHT * 0.4) - int(self.replaySize[1] / 2)), self.replaySize)
        
        self.closeSize = self.menuFont.size("Close")
        self.closeRect = Rect((int(WIDTH * 0.5) - int(self.closeSize[0] / 2), int(HEIGHT * 0.5) - int(self.closeSize[1] / 2)), self.closeSize)
        
        if (self.replayRect.collidepoint(mousePos)):
            screen.blit(self.replayTxtHgl, (self.replayRect.x, self.replayRect.y))
        else:
            screen.blit(self.replayTxt, (self.replayRect.x, self.replayRect.y))
            
        if (self.closeRect.collidepoint(mousePos)):
            screen.blit(self.closeTxtHgl, (self.closeRect.x, self.closeRect.y))
        else:
            screen.blit(self.closeTxt, (self.closeRect.x, self.closeRect.y))

      else:
        heading = self.largeFont.render("Nine Men's Morris", True, YELLOW)
        headingSize = self.largeFont.size("Nine Men's Morris")
        headingPos = (int(WIDTH * 0.5) - int(headingSize[0] / 2),
                           int(HEIGHT * 0.2) - int(headingSize[1] / 2))
        screen.blit(heading, headingPos)

        # Draw highlight if mouse is over an option
        if(self.pvpRect.collidepoint(mousePos)):
            screen.blit(self.pvpTxtHgl, (self.pvpRect.x, self.pvpRect.y))
        else:
            screen.blit(self.pvpTxt, (self.pvpRect.x, self.pvpRect.y))
            
        if(self.pveRect.collidepoint(mousePos)):
            screen.blit(self.pveTxtHgl, (self.pveRect.x, self.pveRect.y))
        else:
            screen.blit(self.pveTxt, (self.pveRect.x, self.pveRect.y))

        if(self.insRect.collidepoint(mousePos)):
            screen.blit(self.insTxtHgl, (self.insRect.x, self.insRect.y))
        else:
            screen.blit(self.insTxt, (self.insRect.x, self.insRect.y))
            
        if(self.exitRect.collidepoint(mousePos)):
            screen.blit(self.exitTxtHgl, (self.exitRect.x, self.exitRect.y))
        else:
            screen.blit(self.exitTxt, (self.exitRect.x, self.exitRect.y))
        
      pygame.display.update()
      
    def handleMenuClick(self, screen, mousePosition):
      if self.isInstructions:
          if self.backRect.collidepoint(mousePosition):
            self.isInstructions = False
      elif self.isEndScreen:
          if self.replayRect.collidepoint(mousePosition):
            self.isEndScreen = False
            #Manual Test 7.1
            #print(“Button has been pressed. Restart Game.”)
          elif self.closeRect.collidepoint(mousePosition):
            #Manual Test 6.1
            #print(“Button has been pressed. Close Program.”)
            pygame.quit()
            sys.exit()
      else:
          if self.pvpRect.collidepoint(mousePosition):
            self.isMenu = False
            #Manual Test 5.1
            #print(“Button has been pressed. Start Game.”)
            self.board.drawBoard()
          elif self.pveRect.collidepoint(mousePosition):
            self.isMenu = False
            self.board.drawBoard()
          elif self.insRect.collidepoint(mousePosition):
            self.isInstructions = True
            #Manual Test 5.2
            #print("Button has been pressed. Instructions Menu Printed.")
          elif self.exitRect.collidepoint(mousePosition):
            pygame.quit()
            sys.exit()

    def drawInstruction(self, instruction, height, screen):
        phrase = self.instructionsFont.render(instruction, True, YELLOW)
        phraseSize = self.instructionsFont.size(instruction)
        phrasePos = (int(WIDTH * 0.5) - int(phraseSize[0] / 2),
                           int(HEIGHT * height) - int(phraseSize[1] / 2))
        screen.blit(phrase, phrasePos)

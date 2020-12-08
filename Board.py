import pygame
import os
import sys
from pygame.locals import *

from Globals import *
import GameLogic

class Board:
    def __init__(self, screen):
        self.screen = screen 
    
        self.turn = 1
        self.currentTurn = "WHITE"
        self.phase1 = True
        self.phase2 = False
        self.phase3White = False
        self.phase3Black = False
        self.removingPiece = False
        self.waiting = True
        self.winner = ""
        self.instructions = "Player WHITE: Place your Piece"
        self.clicked = False
        self.stored = -1
        self.takenSpots = []
        self.blackPlaced = []
        self.whitePlaced = []
        self.boardLeft = int(WIDTH * 0.1)
        self.boardRight = int(WIDTH * 0.9)
        self.middleHorz = int((self.boardRight - self.boardLeft) / 2) + self.boardLeft
        self.boardTop = int(HEIGHT * 0.1)
        self.boardBottom = int(HEIGHT * 0.9)
        self.middleVert = int((self.boardBottom - self.boardTop) / 2) + self.boardTop
        self.midSqLeft = self.middleHorz - int((0.66 *(self.boardRight - self.boardLeft)) / 2)
        self.midSqTop = self.middleVert - int((0.66 *(self.boardBottom - self.boardTop)) / 2)
        self.midSqRight = self.middleHorz + int((0.66 *(self.boardRight - self.boardLeft)) / 2)
        self.midSqBottom = self.middleVert + int((0.66 *(self.boardBottom - self.boardTop)) / 2)
        self.innerSqLeft = self.middleHorz - int((0.33 *(self.boardRight - self.boardLeft)) / 2)
        self.innerSqTop = self.middleVert - int((0.33 *(self.boardBottom - self.boardTop)) / 2)
        self.innerSqRight = self.middleHorz + int((0.33 *(self.boardRight - self.boardLeft)) / 2)
        self.innerSqBottom = self.middleVert + int((0.33 *(self.boardBottom - self.boardTop)) / 2)
        self.axisLeft = int(WIDTH * 0.05)
        self.axisBottom = int(HEIGHT * 0.95)
        self.boardCoords = [(self.boardLeft, self.boardTop), #0
                       (self.boardLeft, self.middleVert), #1
                       (self.boardLeft, self.boardBottom), #2
                       (self.midSqLeft, self.midSqTop), #3
                       (self.midSqLeft, self.middleVert), #4
                       (self.midSqLeft, self.midSqBottom), #5
                       (self.innerSqLeft, self.innerSqTop), #6
                       (self.innerSqLeft, self.middleVert), #7
                       (self.innerSqLeft, self.innerSqBottom), #8
                       (self.middleHorz, self.boardTop), #9
                       (self.middleHorz, self.midSqTop), #10
                       (self.middleHorz, self.innerSqTop), #11
                       (self.middleHorz, self.innerSqBottom), #12
                       (self.middleHorz, self.midSqBottom), #13
                       (self.middleHorz, self.boardBottom), #14
                       (self.innerSqRight, self.innerSqTop), #15
                       (self.innerSqRight, self.middleVert), #16
                       (self.innerSqRight, self.innerSqBottom), #17
                       (self.midSqRight, self.midSqTop), #18
                       (self.midSqRight, self.middleVert), #19
                       (self.midSqRight, self.midSqBottom), #20
                       (self.boardRight, self.boardTop), #21
                       (self.boardRight, self.middleVert), #22
                       (self.boardRight, self.boardBottom)] #23
        
        # Setup Font
        #-------------------------------------------------
        self.wordFont = pygame.font.SysFont(None, 50)

    def drawBoard(self):
        self.screen.fill(GRAY)
        
        instructionsRender = self.wordFont.render(self.instructions, True, YELLOW)
        instructionsSize = self.wordFont.size(self.instructions)
        instructionsPos = (int(WIDTH * 0.5) - int(instructionsSize[0] / 2),
                           int(HEIGHT * 0.05) - int(instructionsSize[1] / 2))
        self.screen.blit(instructionsRender, instructionsPos)

        pygame.draw.rect(self.screen, DUSTY_YELLOW,
                         (self.boardLeft, self.boardTop,
                          self.boardRight - self.boardLeft,
                          self.boardBottom - self.boardTop))

        #coordinates for placing board markers
        textAdj = 12
        axis = {"7": [self.axisLeft, self.boardTop - textAdj], 
                "6":[self.axisLeft, self.midSqTop - textAdj], 
                "5":[self.axisLeft, self.innerSqTop - textAdj], 
                "4":[self.axisLeft, self.middleVert - textAdj], 
                "3":[self.axisLeft, self.innerSqBottom - textAdj], 
                "2":[self.axisLeft, self.midSqBottom - textAdj], 
                "1":[self.axisLeft, self.boardBottom - textAdj], 
                "a":[self.boardLeft - textAdj, self.axisBottom], 
                "b":[self.midSqLeft - textAdj, self.axisBottom], 
                "c":[self.innerSqLeft - textAdj, self.axisBottom], 
                "d":[self.middleHorz - textAdj, self.axisBottom], 
                "e":[self.innerSqRight - textAdj, self.axisBottom], 
                "f":[self.midSqRight - textAdj, self.axisBottom], 
                "g":[self.boardRight - textAdj, self.axisBottom],}

        for items in axis:
            text = self.wordFont.render(items, True, (YELLOW))
            self.screen.blit(text, axis[items])

        for idx in range(0, len(self.boardCoords)):
            pygame.draw.circle(self.screen, BLACK,
                (self.boardCoords[idx][0], self.boardCoords[idx][1]), 5)

        pieceSize = 15

        if self.clicked:
            pygame.draw.circle(self.screen, YELLOW,
                (self.boardCoords[self.stored][0], self.boardCoords[self.stored][1]), pieceSize+3)

        for piece in self.blackPlaced:
            pygame.draw.circle(self.screen, BLACK,
                (self.boardCoords[piece][0], self.boardCoords[piece][1]), pieceSize)

        for piece in self.whitePlaced:
            pygame.draw.circle(self.screen, WHITE,
                (self.boardCoords[piece][0], self.boardCoords[piece][1]), pieceSize - 1)
            pygame.draw.circle(self.screen, BLACK,
                (self.boardCoords[piece][0], self.boardCoords[piece][1]), pieceSize, 1)


        lineWidth = 3
        pygame.draw.line(self.screen, BLACK, (self.boardLeft, self.boardTop),
                         (self.boardLeft, self.boardBottom), lineWidth)
        pygame.draw.line(self.screen, BLACK, (self.boardLeft, self.boardTop),
                         (self.boardRight, self.boardTop), lineWidth)
        pygame.draw.line(self.screen, BLACK, (self.boardLeft, self.boardBottom),
                         (self.boardRight, self.boardBottom), lineWidth)
        pygame.draw.line(self.screen, BLACK, (self.boardRight, self.boardTop),
                         (self.boardRight, self.boardBottom), lineWidth)

        pygame.draw.line(self.screen, BLACK, (self.midSqLeft, self.midSqTop),
                         (self.midSqLeft, self.midSqBottom), lineWidth)
        pygame.draw.line(self.screen, BLACK, (self.midSqLeft, self.midSqTop),
                         (self.midSqRight, self.midSqTop), lineWidth)
        pygame.draw.line(self.screen, BLACK, (self.midSqLeft, self.midSqBottom),
                         (self.midSqRight, self.midSqBottom), lineWidth)
        pygame.draw.line(self.screen, BLACK, (self.midSqRight, self.midSqTop),
                         (self.midSqRight, self.midSqBottom), lineWidth)

        pygame.draw.line(self.screen, BLACK, (self.innerSqLeft, self.innerSqTop),
                         (self.innerSqLeft, self.innerSqBottom), lineWidth)
        pygame.draw.line(self.screen, BLACK, (self.innerSqLeft, self.innerSqTop),
                         (self.innerSqRight, self.innerSqTop), lineWidth)
        pygame.draw.line(self.screen, BLACK, (self.innerSqLeft, self.innerSqBottom),
                         (self.innerSqRight, self.innerSqBottom), lineWidth)
        pygame.draw.line(self.screen, BLACK, (self.innerSqRight, self.innerSqTop),
                         (self.innerSqRight, self.innerSqBottom), lineWidth)

        pygame.draw.line(self.screen, BLACK, (self.boardLeft, self.middleVert),
                         (self.innerSqLeft, self.middleVert), lineWidth)
        pygame.draw.line(self.screen, BLACK, (self.innerSqRight, self.middleVert),
                         (self.boardRight, self.middleVert), lineWidth)
        pygame.draw.line(self.screen, BLACK, (self.middleHorz, self.boardTop),
                         (self.middleHorz, self.innerSqTop), lineWidth)
        pygame.draw.line(self.screen, BLACK, (self.middleHorz, self.innerSqBottom),
                         (self.middleHorz, self.boardBottom), lineWidth)

        pygame.display.update()
  
    def handleMouseClick(self, s, t):
        pieceLocation = self.convertCoordinatesNUM(s, t)
        self.currentTurn = self.turnCheck()
        
        if self.removingPiece:
            if self.currentTurn == "WHITE":
                if self.isBlackPiece(pieceLocation):
                    self.blackPlaced.remove(pieceLocation)
                    self.takenSpots.remove(pieceLocation)
                    if self.phase2 and len(self.blackPlaced) == 3:
                        self.phase3Black = True
                    self.instructionText()
                    self.turn = self.turn + 1
                    self.waiting = True
                    self.removingPiece = False
            elif self.currentTurn == "BLACK":
                if self.isWhitePiece(pieceLocation):
                    self.whitePlaced.remove(pieceLocation)
                    self.takenSpots.remove(pieceLocation)
                    if self.phase2 and len(self.whitePlaced) == 3:
                        self.phase3White = True
                    self.instructionText()
                    self.turn = self.turn + 1
                    self.waiting = True
                    self.removingPiece = False
        elif self.phase1:
            if self.isNotTaken(pieceLocation):
                self.instructionText()
                self.phaseOne(pieceLocation)
                #print("Phase 1 in progress, Valid piece placed.")
            #print("Phase 1 in progress, Invalid piece not placed.")
        elif  self.currentTurn == "BLACK" and self.phase3Black:
            if self.convertCoordinatesNUM(s, t) == self.stored:
                self.stored = -1
                self.clicked = False
            elif self.clicked == False:
            	self.clickOne(pieceLocation)
            else:
            	if self.isNotTaken(pieceLocation):
                    self.instructionText()
                    self.clickTwo(pieceLocation)
                    #print("Phase 3 in progress, Valid black piece placed.")
                #print("Phase 3 in progress, Invalid black piece not placed.")
        elif  self.currentTurn == "WHITE" and self.phase3White:
            if self.convertCoordinatesNUM(s, t) == self.stored:
                self.stored = -1
                self.clicked = False
            elif self.clicked == False:
                self.clickOne(pieceLocation)
            else:
            	if self.isNotTaken(pieceLocation):
                    self.instructionText()
                    self.clickTwo(pieceLocation)
                    #print("Phase 3 in progress, Valid white piece placed.")
                #print("Phase 3 in progress, Invalid white piece not placed.")
        elif self.phase2:
            if self.convertCoordinatesNUM(s, t) == self.stored:
                self.stored = -1
                self.clicked = False
            elif self.clicked == False:
                self.clickOne(pieceLocation)
            else:
                if self.isNotTaken(pieceLocation) and GameLogic.isAdj(self.stored ,pieceLocation):
                    self.instructionText()
                    self.clickTwo(pieceLocation)
                    #print("Phase 2 in progress, Valid piece placed.")
                #print("Phase 2 in progress, Invalid piece not placed.")

                
        if self.removingPiece:
            if self.waiting:
                self.turn = self.turn - 1
                self.waiting = False
            self.instructions = ("Player " + self.turnCheck() + ": Remove a Piece")
        
        self.drawBoard() 

        #COMPUTER IF STATEMENT GOES HERE 

        return self.hasWon()

      
    def hasWon(self):
        if self.phase1 == False:
            if len(self.whitePlaced) == 2:
                self.winner = "BLACK"
                return True
            elif len(self.blackPlaced) == 2:
                self.winner = "WHITE"
                return True
        return False
    
    def turnCheck(self):
        if self.turn % 2 == 0:                                
            return "BLACK"
        else:
            return "WHITE"
  
    def instructionText(self):
        if self.currentTurn == "WHITE" and self.phase3Black:
            self.instructions = ("Player BLACK: Move your Piece (Flying Phase)")
        elif self.currentTurn == "BLACK" and self.phase3White:
            self.instructions = ("Player WHITE: Move your Piece (Flying Phase)")
        elif self.currentTurn == "WHITE" and self.phase2:
            self.instructions = ("Player BLACK: Move your Piece")
        elif self.currentTurn == "BLACK" and self.phase2:
            self.instructions = ("Player WHITE: Move your Piece")
        elif self.currentTurn == "WHITE" and self.phase1:
            self.instructions = ("Player BLACK: Place your Piece")
        elif self.currentTurn == "BLACK" and self.phase1:
            self.instructions = ("Player WHITE: Place your Piece")
      
    def convertCoordinatesNUM(self, s, t):
        locationNum = GameLogic.cordsToNum(s, t, self.boardCoords) 
        return locationNum
    
    def isNotTaken(self, num):
        if num in self.takenSpots:
            return False
        return True
  
    def isBlackPiece(self, num):
        if num in self.blackPlaced:
            return True
        return False
  
    def isWhitePiece(self, num):
        if num in self.whitePlaced:
            return True
        return False
    
    def phaseOne(self, location):
        if self.currentTurn == "BLACK":                             
            self.blackPlaced.append(location)
            self.drawBoard()
            if GameLogic.isMill(self.blackPlaced, location):
                self.removingPiece = True
        else:
            self.whitePlaced.append(location)
            self.drawBoard()
            if GameLogic.isMill(self.whitePlaced, location):
                self.removingPiece = True
                    
        self.turn = self.turn + 1
        if self.turn == 19:
            self.phase1 = False
            self.phase2 = True
            self.instructions = ("Player WHITE: Move your Piece")
        self.takenSpots.append(location)
    
    def clickOne(self, pieceLocation):
        if self.currentTurn == "BLACK":
            if self.isBlackPiece(pieceLocation):
                self.stored = pieceLocation
                self.clicked = True
        else:
            if self.isWhitePiece(pieceLocation):
                self.stored = pieceLocation
                self.clicked = True
    
    def clickTwo(self, pieceLocation):
        if self.currentTurn == "BLACK":
            self.blackPlaced.append(pieceLocation)
            self.blackPlaced.remove(self.stored)
            self.takenSpots.append(pieceLocation)
            self.takenSpots.remove(self.stored)
            self.stored = -1
            self.turn = self.turn + 1
            self.clicked = False
            if GameLogic.isMill(self.blackPlaced, pieceLocation):
                self.removingPiece = True
        else:
            self.whitePlaced.append(pieceLocation)
            self.whitePlaced.remove(self.stored)
            self.takenSpots.append(pieceLocation)
            self.takenSpots.remove(self.stored)
            self.stored = -1
            self.turn = self.turn + 1
            self.clicked = False
            if GameLogic.isMill(self.whitePlaced, pieceLocation):
                self.removingPiece = True
    
    def clearBoard(self):
        self.turn = 1
        self.currentTurn = "WHITE"
        self.phase1 = True
        self.phase2 = False
        self.phase3White = False
        self.phase3Black = False
        self.removingPiece = False
        self.waiting = True
        self.winner = ""
        self.instructions = "Player WHITE: Place your Piece"
        self.clicked = False
        self.stored = -1
        self.takenSpots = []
        self.blackPlaced = []
        self.whitePlaced = []
        self.drawBoard()
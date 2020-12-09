import pygame
import os
import sys
import random
from pygame.locals import *

from Board import *
import GameLogic

def getOpenSpots(takenSpots):
    spots = []
    for i in range(0,24):
        spots.append(i)

    openSpots = [x for x in spots if x not in takenSpots]

    return openSpots

def pickByRandom(options):
    return random.choice(options)

def makeOrPreventMill(potentialSpots, blackPlaced, whitePlaced):
    moveOptions = []
    for i in potentialSpots:
        blackPlaced.append(i)
        whitePlaced.append(i)
        
        if GameLogic.isMill(blackPlaced, i) or GameLogic.isMill(whitePlaced, i):
            print("i:", i)
            moveOptions.append(i)
        blackPlaced.remove(i)
        whitePlaced.remove(i)
        i += i
    return moveOptions


def closeMills(spot):
        listOfSpots = []

        millList = [[{0,1,2}, {0,9,21}], #0
                 [{0,1,2}, {1,4,7}], #1
                 [{0,1,2}, {2,14,23}], #2
                 [{3,4,5}, {3,10,18}], #3
                 [{3,4,5}, {1,4,7}], #4
                 [{3,4,5}, {5,13,20}], #5
                 [{6,7,8}, {6,11,15}], #6
                 [{6,7,8}, {1,4,7}], #7
                 [{6,7,8}, {8,12,17}], #8
                 [{9,10,11}, {0,9,21}], #9
                 [{9,10,11}, {3,10,18}], #10
                 [{9,10,11}, {6,11,15}], #11
                 [{12,13,14}, {8,12,17}], #12
                 [{12,13,14}, {5,13,20}], #13
                 [{12,13,14}, {2,14,23}], #14
                 [{15,16,17}, {6,11,15}], #15
                 [{15,16,17}, {16,19,22}], #16
                 [{15,16,17}, {8,12,17}], #17
                 [{18,19,20}, {3,10,18}], #18
                 [{18,19,20}, {16,19,22}], #19
                 [{18,19,20}, {5,13,20}], #20
                 [{21,22,23}, {0,9,21}], #21
                 [{21,22,23}, {16,19,22}], #22
                 [{21,22,23}, {2,14,23}]] #23

        for mill in millList[spot]:
            listOfSpots = listOfSpots + list(mill)
        return listOfSpots

def potentialMill(available, placed):

    allCloseMills = []

    for piece in placed:
        allCloseMills = allCloseMills + closeMills(piece)

    options = [x for x in allCloseMills if x in available]

    return options

def findOpenNeighbors(openSpots, spot):
    neighbors = []
    for i in openSpots:
        if GameLogic.isAdj(spot, i):
            neighbors.append(i)
    return neighbors

def allPossibleMoves(openSpots, blackPlaced):

    possibleMoves = {}
    
    for piece in blackPlaced:
        neigh = findOpenNeighbors(openSpots, piece)
        if len(neigh)!=0:
            possibleMoves[piece] = neigh

    return possibleMoves

def phase2Mill(moves, blackPlaced, whitePlaced):
    allOptions = {}
    for piece in moves:
        allOptions[piece] = makeOrPreventMill(moves[piece], blackPlaced, whitePlaced)

    removeKeys = []

    for key in allOptions:
        if len(allOptions[key]) == 0:
            removeKeys.append(key)
    [allOptions.pop(key) for key in removeKeys] 

    return allOptions

def phase2CloseMill(moves, openSpots, blackPlaced, whitePlaced):
    allOptions = {}

    for piece in moves:
        potMillSpots = potentialMill(openSpots, blackPlaced)

    for piece in moves:
        allOptions[piece] = [x for x in moves[piece] if x in potMillSpots]

    removeKeys = []

    for key in allOptions:
        if len(allOptions[key]) == 0:
            removeKeys.append(key)
    [allOptions.pop(key) for key in removeKeys] 

    return allOptions


def AIphase2(takenSpots, whitePlaced, blackPlaced):
    openSpots = getOpenSpots(takenSpots)
    moves = allPossibleMoves(openSpots, blackPlaced)
    print(moves)

    options = []
    options = phase2Mill(moves, blackPlaced, whitePlaced)
    if len(options)!=0:
        print("opt 1: ", options)
        oldSpot, newSpot = pickByRandom(list(options.items()))
        return oldSpot,newSpot[0]

    options = phase2CloseMill(moves, openSpots, blackPlaced, whitePlaced)
    if len(options)!=0:
        print("opt 2: ", options)

        oldSpot, newSpot = pickByRandom(list(options.items()))
        return oldSpot,newSpot[0]

    else:
        print("opt 3: ", options)

        oldSpot, newSpot = pickByRandom(list(moves.items()))
    return oldSpot, newSpot[0]


def removal(whitePlaced, blackPlaced):
    options = []
    options = makeOrPreventMill(whitePlaced, blackPlaced, whitePlaced)
    if len(options) != 0:
        return pickByRandom(options)

    options = potentialMill(whitePlaced, whitePlaced)
    if len(options)!=0:
        return pickByRandom(options)

    else:
        return pickByRandom(whitePlaced)

def AIPhase1(takenSpots, whitePlaced, blackPlaced):
    openSpots = getOpenSpots(takenSpots)

    if len(blackPlaced) == 0:
        return pickByRandom(openSpots)

    moveOptions = makeOrPreventMill(openSpots, blackPlaced, whitePlaced)
    if len(moveOptions) != 0:
        return pickByRandom(moveOptions)
        
    moveOptions = potentialMill(openSpots, blackPlaced)
    if len(moveOptions) != 0:
        return pickByRandom(moveOptions)

def AIFlying(takenSpots, whitePlaced, blackPlaced):
     openSpots = getOpenSpots(takenSpots)

     moveFrom = pickByRandom(blackPlaced)

     options = []
     options = makeOrPreventMill(openSpots, blackPlaced, whitePlaced)
     if len(options) != 0:
        moveTo = pickByRandom(options)
        return moveFrom, moveTo

     options = potentialMill(openSpots, blackPlaced)
     if len(options) != 0:
        moveTo = pickByRandom(options)
        return moveFrom, moveTo
    
     else:
        return pickByRandom(blackPlaced), pickByRandom(openSpots)

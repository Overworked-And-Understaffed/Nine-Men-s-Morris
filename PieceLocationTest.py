
import pygame
from ninemm.py import *

def main():
    run = True
    clock = pygame.time.Clock()
    while run:
        spots = make_board()
        clock.tick(FPS)
        Piece_Location_Test(spots)


def  Piece_Location(x, y, spots_Dict):
    xy_range = 25

    for i in spots_Dict.values():
        if (i[0] > x - xy_range and i[0] < x + xy_range and i[1] > y - xy_range and i[1] < y + xy_range):
            return True
        else:
            return False


def Piece_Location_Test(spots_Dict):
    xy_range = 25
    
    for x in range(800):
        for y in range(800):
            for is in spots_Dict.values():
                if (i[0] > x - xy_range and i[0] < x + xy_range and i[1] > y - xy_range and i[1] < y + xy_range):
                    assert Piece_Location(x, y, spots_Dict) == True
                else:
                    assert Piece_Location(x, y, spots_Dict) == False
                    
    print("End")
    return 

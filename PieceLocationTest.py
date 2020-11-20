import unittest
import pygame
import Board
from GameLogic import cordsToNum

class PieceLocationTest(unittest.TestCase):
    def Piece_Location(self, x, y, spots_List):
        if cordsToNum(x, y, spots_List) == -1:
            return False
        else: 
            return True


    def test_Piece_Location_Test(self):
        xy_range = 25
        
        for x in range(800):
            for y in range(800):
                for i in Board.boardCoords.values():
                    if (i[0] > x - xy_range and i[0] < x + xy_range and i[1] > y - xy_range and i[1] < y + xy_range):
                        assert Piece_Location(x, y, Board.boardCoords) == True
                    else:
                        assert Piece_Location(x, y, Board.boardCoords) == False
                        
        print("End")
        return 

if __name__ == '__main__':
    unittest.main()
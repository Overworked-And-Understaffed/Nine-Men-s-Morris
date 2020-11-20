import unittest
import Main
import pygame
import Board

class CheckTurnTest(unittest.TestCase):
    def test_CheckTurnTest(self):
        for player_turn in range(101):
            Board.turn = player_turn
            if (player_turn % 2 == 0):
                # assert Player = Player A
                self.assertEqual(Board.turnCheck(),"BLACK")
            else:
                # assert Player = Player B
                self.assertEqual(Board.turnCheck(),"WHITE")
        print("End")
        return 
                
if __name__ == '__main__': 
    unittest.main() 
                
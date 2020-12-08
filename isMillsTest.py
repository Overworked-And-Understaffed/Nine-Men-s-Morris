import unittest
from GameLogic import isMill

class CheckMillTest(unittest.TestCase):
    def testCheckMillTest(self):
        millsList = [[0,1,2],[3,4,5],[6,7,8],[9,10,11],[12,13,14],[15,16,17],[18,19,20],[21,22,23],[0,9,21],[3,10,18],[6,11,15],[1,4,7],[16,19,22],[8,12,17],[5,13,20],[2,14,23]]
        for firstPiece in range(23):
            for secondPiece in range(23):
                if firstPiece != secondPiece:
                    for thirdPiece in range(23):
                        if thirdPiece != secondPiece and thirdPiece != firstPiece:
                            print('\n',firstPiece,secondPiece,thirdPiece)
                            testList = sorted([firstPiece,secondPiece,thirdPiece])
                            if testList in millsList:
                                assert isMill([firstPiece,secondPiece,thirdPiece],thirdPiece) == True 
                                print("True")
                            else:
                                self.assertFalse(isMill([firstPiece,secondPiece],thirdPiece))
                                print("False")
        print("End")

if __name__ == '__main__': 
    unittest.main() 
    assert isMill([firstPiece,secondPiece],thirdPiece) == False
    print(sorted({firstPiece,secondPiece,thirdPiece}))
    print("End")

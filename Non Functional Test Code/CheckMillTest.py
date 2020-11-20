from Main import isMill

def CheckMillTest ():
    mill_list = [{0,1,2},{3,4,5},{6,7,8},{9,10,11},{12,13,14},{15,16,17},{18,19,20},{21,22,23},{0,9,21},{3,10,18},{6,11,15},{1,4,7},{16,19,22},{8,12,17},{5,13,20},{2,14,23}]
    for firstPiece in range(23):
        for secondPiece in range(23):
            if firstPiece != secondPiece:
                for thirdPiece in range(23):
                    if thirdPiece != secondPiece and thirdPiece != firstPiece:
                        print('\n',firstPiece,secondPiece,thirdPiece)
                        if sorted({firstPiece,secondPiece,thirdPiece}) in mill_list:
                            assert isMill([firstPiece,secondPiece],thirdPiece) == True
                            print("True")
                        else:
                            assert isMill([firstPiece,secondPiece],thirdPiece) == False
                            print("False")
    print("End")
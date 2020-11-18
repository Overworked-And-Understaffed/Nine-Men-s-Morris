import pygame
import os
import sys
from pygame.locals import *
  
'''def Piece_Location(x, y, spots_Dict):
        
        xy_range = 25
        # Range set to 25, could be changed, seems good
        
        for i in spots_Dict.values():
            if (i[0] > x - xy_range and i[0] < x + xy_range and i[1] > y - xy_range and i[1] < y + xy_range):
                print(x, y, i[0], i[1])
                print("YEAH BOI") #Love it
                return [i[0],i[1]]
        else:
            return [0,0]'''
          
def cordsToNum(x, y, spots_List):       
    xy_range = 25
    # Range set to 25, could be changed, seems good
    
    for i in range(0, len(spots_List)):
        if (spots_List[i][0] > x - xy_range and spots_List[i][0] < x + xy_range
            and spots_List[i][1] > y - xy_range and spots_List[i][1] < y + xy_range):
            return i
        
    return -1

'''def numToCords(num, spots_Dict):
        
    for key, value in spots_Dict.items():
        if (key == num):
            return value'''

def isMill(placed_pieces, new_piece):

    mill_list = [[{0,1,2}, {0,9,21}], #0
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

    for mill in mill_list[new_piece]:
        if mill.issubset(placed_pieces):
            return True

    return False

def isAdj(current_spot, potential_spot):
    adjacent_positions = [{1,9},#0
                          {0,4,2},#1
                          {1,14},#2
                          {10,4},#3
                          {1,3,5,7},#4
                          {4,3},#5
                          {11,7},#6
                          {6,8,4},#7
                          {7,12},#8
                          {0,21,10},#9
                          {3,9,18,11},#10
                          {10,6,15},#11
                          {8,17,13},#12
                          {12,5,20,14},#13
                          {13,2,23},#14
                          {11,16},#15
                          {15,19,17},#16
                          {16,12},#17
                          {10,19},#18
                          {18,16,22,20},#19
                          {19,13},#20
                          {9,22},#21
                          {21,19,23},#22
                          {22,14}]#23

    if potential_spot in adjacent_positions[current_spot]:
        return True
    else:
        return False               
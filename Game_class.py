#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
import os
import sys
from pygame.locals import *
import pygame_menu
from pygame_menu.widgets.core.widget import Widget

pygame.init()

#Colour Palette
BLACK = (0,0,0)
WHITE = (255,255,255)
JOSHY_GREY = (160,180,180)
IZZY_RED = (255,0,50)
GRAY = (100,100,100)
YELLOW = (255,240,0)
DUSTY_YELLOW = (200,230,180)
FPS = 60

#Screen info
WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT)) #Window size
pygame.display.set_caption("Nine Men's Morris Game") #Window title
screen.fill(GRAY)
pygame.draw.rect(screen, DUSTY_YELLOW, (100, 100, 600, 600))
clock = pygame.time.Clock()

#pygame.RESIZABLE

#wall_writing
word_font = pygame.font.SysFont(None, 50)
instructions_font = pygame.font.SysFont(None, 30)
menu_font = pygame.font.SysFont(None, 25)

class Game(object):
    def __init__(self):
        #self.color = color
        self.Main()
        ##self.menu = MAIN_MENU
    
    def multiplayer(self):
        print("you've chosen to play with a friend")
        pass
    
    def AI(self):
        print("You've chosen to play against the computer")
        pass
    
    def rules(self):
        print("OooOOoOO we could list the rules here ig. whatcha guys think??")
        pass
    
    def idek_mane(self, values, something):
        self.values = values
        self.something = something
        print("welp this is here too")
        pass

    def Main(self):
        #variables
        turn = 1    #TRACK TURNS
        phase = 1
        selected = 123
        black_count = 0    #
        white_count = 0    #TRACK NO. PIECES
        taken_spots = []    #TRACK NON-AVAILABLE SPOTS
        black_placed = []
        white_placed = []
        mill = False

        #mainloop===========================
        
        run = True
        clock = pygame.time.Clock()
        valid_point = instructions_font.render("Select an edge to start PLAY...", True, (YELLOW))
        screen.blit(valid_point, [290,40])
        
        while run:
            clock.tick(60)
            screen.fill(GRAY)
            
            #exits game on request
            for event in pygame.event.get():
                mouse_position = pygame.mouse.get_pos()
                if event.type == pygame.QUIT:
                    run = False

                spots = Board.make_board(self)
                Board.redraw_pieces(self, black_placed, white_placed, spots)

                #search for user/mouse input
                if event.type == pygame.MOUSEBUTTONDOWN:

                    if turn == 19:
                        phase = 2
                        print("PHASE 2 - SELECT a piece to move")
                    
                    s, t = mouse_position
                    [x, y] = Board.Piece_Location(self, s, t, spots)
                    location_num = Board.cordsToNum(self, x, y, spots) 
                    
                    if mill == True:
                        print(COLOR, " select opponenets piece to be removed")
                        if COLOR == BLACK and location_num in white_placed:
                            pygame.draw.circle(screen, IZZY_RED, (x,y), 30)
                            pygame.draw.circle(screen, WHITE, (x, y), 20)
                            taken_spots.remove([x,y])
                            white_placed.remove(location_num)
                            mill = False
                        elif COLOR == WHITE and location_num in black_placed:
                            pygame.draw.circle(screen, IZZY_RED, (x,y), 30)
                            pygame.draw.circle(screen, BLACK, (x, y), 20)
                            taken_spots.remove([x,y])
                            black_placed.remove(location_num)
                            mill = False
                        else:
                            pass

                    elif phase == 2:

                        if turn % 2 == 0:                                
                            COLOR = BLACK
                        else:
                            COLOR = WHITE

                        if selected != 123:

                            sel = Board.numToCords(self, selected, spots)
                            pygame.draw.circle(screen, YELLOW, sel, 30)
                            pygame.draw.circle(screen, COLOR, (x, y), 20)

                            move_to = location_num

                            print("selected", selected)
                            print("MOVE TO", move_to)

                            if ([x,y] not in taken_spots and [x,y] != [0,0] and Board.isAdj(self,selected, move_to) == True):
                                print("are we even getting to this part")

                                if COLOR == BLACK:
                                    pygame.draw.circle(screen, BLACK, (x, y), 20)
                                    print("Black",location_num)
                                    black_placed.remove(selected)
                                    mill = Board.isMill(self, black_placed, move_to)

                                else:
                                    pygame.draw.circle(screen, WHITE, (x, y), 20)
                                    print("White", location_num)
                                    white_placed.remove(selected)
                                    mill = Board.isMill(self, white_placed, move_to)

                                turn = turn + 1
                                taken_spots.append([x,y])
                                taken_spots.remove(sel)
                                print("black spots:", black_placed)
                                print("white spots:", white_placed)
                                selected = 123
                            else:
                                pass

                        else:
                           if location_num in black_placed or location_num in white_placed:
                                selected = location_num
                           else:
                                continue
                        
                    # Phase 1 - placing 9 pieces each
                    else:
                    #do nothing if spot is not available
                        if [x, y] in taken_spots:
                            print ("----> Position not Empty <----")
                            continue

                        #condition for if spot is available
                            #Test of taken_spots
                            #print("Piece has already been placed!")
                    
                        #if spot is available
                        else:
                            pygame.draw.rect(screen, GRAY, (0,0,800,70)) #erase and replace exiting text of text
                        
                            #keep total game pieces to 18, 9 for each player
                            if black_count == 9 and white_count == 9:
                                #==================================
                                #where the action happens
                                #==================================
                                pass 

                            #conditions to determine player turns and player count
                            else:
                                #BLACK PLACEMENT
                                if turn % 2 == 0:                                
                                    COLOR = BLACK
                                    # display_blacksTurn = word_font.render("Player B", True, (YELLOW))
                                    # screen.blit(display_blacksTurn, [650,30])  

                                #WHITE PLACEMENT
                                else:
                                    COLOR = WHITE
                                    # display_whitesTurn = word_font.render ("Player A", True, (YELLOW))
                                    # screen.blit(display_whitesTurn, [650,30])  
                               
                                #should this build be in seperate conditions above?
                                if [x,y] != [0,0]: 
                                    pygame.draw.circle(screen, BLACK, (x, y), 20)
                                    pygame.draw.circle(screen, COLOR, (x, y), 18)
                                    if COLOR == BLACK:
                                        black_count += 1
                                        black_to_move = instructions_font.render("Player B: Waiting for White Piece...", True, (YELLOW))
                                        screen.blit(black_to_move, [200,50])   
                                        pygame.draw.circle(screen, BLACK, (x+5, y-3), 2)
                                        mill = Board.isMill(self, black_placed, location_num)
                                        #black_placed.append(location_num)
                                    else:
                                        white_count += 1
                                        white_to_move = instructions_font.render("Player A: Waiting for Black Piece...", True, (YELLOW))
                                        screen.blit(white_to_move, [200,50])
                                        pygame.draw.circle(screen, WHITE, (x+2, y-3), 2)
                                        mill = Board.isMill(self, white_placed, location_num)
                                        #white_placed.append(location_num)

                                    #my isMill function automatically updates the black/white_placed lists..? im not sure why .____.
                                    turn = turn + 1
                                    taken_spots.append([x,y])
                                    #print("black spots:", black_placed)
                                    #print("white spots:", white_placed)
                    
                        print ("White currently has {} pieces on board at {}!".format(white_count, white_placed))
                        print ("Black currently has {} pieces on board at {}!\n".format(black_count, black_placed)) 

class Board(object):
    def __init__(self):
        super().__init__()
        
    def make_board(self):
        #instruction menu
        pygame.draw.rect(screen, BLACK, (725, 500, 50, 20))
        help_button = menu_font.render("Help", True, (YELLOW))
        screen.blit(help_button, [730,500])
        
        pygame.draw.rect(screen, BLACK, (725, 400, 50, 20))
        help_button = menu_font.render("Menu", True, (YELLOW))
        screen.blit(help_button, [730, 400])
            
        #coordinates for placing board markers
        axis = {"7": [60, 95], "6":[60, 195], "5":[60, 295], "4":[60, 395], "3":[60, 495], "2":[60, 595], "1":[60, 695], "a": [95, 720], "b":[195, 720], "c":[295, 720], "d":[395, 720], "e":[495, 720], "f":[595, 720], "g":[695, 720],}
        for items in axis:
            text = word_font.render(items, True, (YELLOW))
            screen.blit(text, axis[items])


        color = BLACK
        board_coords1 = [600,400,200]
        board_coords2 = [100,200,300]
        spots = [] #cell coordinates list
        i = 0
        
        while i < 3:
            x = board_coords2[i]
            y = board_coords1[i]

           #setup circle placeholders
            pygame.draw.circle(screen, color, (x,x), 5)
            spots.append([x,x])

            pygame.draw.circle(screen, color, (y+x,y+x), 5)
            spots.append([y+x,y+x])

            pygame.draw.circle(screen, color, (y+x,x), 5)
            spots.append([y+x,x])

            pygame.draw.circle(screen, color, (x,y+x), 5)
            spots.append([x,y+x])

            pygame.draw.circle(screen, color, (x, 400), 5)
            spots.append([x, 400])

            pygame.draw.circle(screen, color, (y+x, 400), 5)
            spots.append([y+x, 400])

            pygame.draw.circle(screen, color, (400, x), 5)
            spots.append([400, x])

            pygame.draw.circle(screen, color, (400, x+y), 5)
            spots.append([400, x+y])
        
        
            #draws the long lines
            pygame.draw.line(screen, color, (x,x), (x,y+x), 5)
            pygame.draw.line(screen, color, (y+x,x), (y+x,y+x), 5)
            pygame.draw.line(screen, color, (x,x), (y+x,x), 5)
            pygame.draw.line(screen, color, (x,y+x), (y+x,y+x), 5)

            i=i+1
        
        #draws the short lines
        pygame.draw.line(screen, color, (board_coords2[0],400), (board_coords2[2],400), 5) #a4 - c4
        pygame.draw.line(screen, color, (board_coords2[0]+board_coords1[0],400), (board_coords2[2]+board_coords1[2],400), 5) #e4 - g4
        pygame.draw.line(screen, color, (400,board_coords2[0]), (400,board_coords2[2]), 5) #d7 - d5
        pygame.draw.line(screen, color, (400,board_coords2[0]+board_coords1[0]), (400,board_coords2[2]+board_coords1[2]), 5) #d3-d1
   
        pygame.display.flip()

        spots.sort() #sorts list of locations before the data goes into a dictionary 

        #makes a dictionary to number each spot location
        spots_Dict = {}
        for a, b in enumerate(spots): 
            spots_Dict[a] = b

        #print(spots_Dict)
        #Looks like {0: [100, 100], 1: [100, 400], 2: [100, 700], 3:[200,200]...}
        return spots_Dict

    def redraw_pieces(self, black, white, spots_Dict):
        for i in black:
            [x,y] = Board.numToCords(self, i, spots_Dict)
            pygame.draw.circle(screen, BLACK, (x, y), 20)
        for i in white:
            [x,y] = Board.numToCords(self, i, spots_Dict)
            pygame.draw.circle(screen, WHITE, (x, y), 20)
    
    def Piece_Location(self, x, y, spots_Dict):
        xy_range = 25
        # Range set to 25, could be changed, seems good
        
        for i in spots_Dict.values():
            if (i[0] > x - xy_range and i[0] < x + xy_range and i[1] > y - xy_range and i[1] < y + xy_range):
                print(x, y, i[0], i[1])
                print("YEAH BOI") #Love it
                return [i[0],i[1]]
        else:
            return [0,0]
        
    def cordsToNum(self, x, y, spots_Dict):
        
        for key, value in spots_Dict.items():
            if (value[0] == x and value[1] == y):
                return key

    def numToCords(self, num, spots_Dict):
        
        for key, value in spots_Dict.items():
            if (key == num):
                return value

    def isMill(self, placed_pieces, new_piece):
    #print(placed_pieces)
        mill_list = [{0,1,2},{3,4,5},{6,7,8},{9,10,11},{12,13,14},{15,16,17},{18,19,20},{21,22,23},{0,9,21},{3,10,18},{6,11,15},{1,4,7},{16,19,22},{8,12,17},{5,13,20},{2,14,23}]
    
    #First dicards mills from past turns 
        for mill in mill_list:
            if mill.issubset(placed_pieces):
                mill_list.remove(mill)
    
        placed_pieces.append(new_piece)

    #Now considers if the new piece created a mill
    
        for mill in mill_list:
            if mill.issubset(placed_pieces):
                print("Mill at:", mill)
                return True
        print("No mill rn bruh")
        return False

    def isAdj(self, current_spot, potential_spot):
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
                            {22,14},#23
                            ]
        if potential_spot in adjacent_positions[current_spot]:
            return True
        else:
            return False
 

        
    #menu

class Piece:
    #color attribute
    def init(self, color, x, y):
        self.color = color
        self.location_x = x
        self.location_y = y
        self.is_alive = True

    def str(self):
        return self.color[0]

    def update_location(self, x, y):
        self.location_x = x
        self.location_y = y

    def kill(self):
        self.is_alive = False


game_menu = pygame_menu.Menu(WIDTH, HEIGHT-200, "Menu", theme = pygame_menu.themes.THEME_SOLARIZED, mouse_enabled=True)

help_menu = pygame_menu.Menu(WIDTH-150, HEIGHT, "Instructions", center_content= True, theme = pygame_menu.themes.THEME_BLUE)
help_menu.add_label("This is an abstract stategy board game with 2 players.")
help_menu.add_label("Each player has 9 pieces, taking turns placing.")
help_menu.add_label("The goal is to get your opponent down to 2 pieces only.")
help_menu.add_label("To accomplish this...", background_color=(70, 100, 120))
help_menu.add_label("Get 3 of your pieces on one line to create a 'mill'.")
help_menu.add_label("Once you create a mill, you can then remove")
help_menu.add_label("one of your opponent's pieces from the board. ") #There are multiple phases to the game:\n\n\nThe 'Placing Pieces' Phase: This phase allows you and your opponent to, in turns, place all of your pieces on the board.\n\nThe 'Moving Pieces' Phase: Once all of the pieces are placed on the board, both you and your opponent try to move your pieces into mills to remove your opponents pieces. During this phase, you can only move your pieces to any places on the board ajacent to where your piece currently is that also has no other pieces placed there.\nThe 'Flying' Phase: When either you or your opponent is down to three pieces, on their turn, that player can move their pieces anywhere on the board where there is not already another piece.")
help_menu.add_button("Back", game_menu, pygame_menu.events.CLOSE)


#game_menu.add_label("Nine Men's Morris Game")

game_menu.add_button('Play', pygame_menu.Menu, Game())
game_menu.add_button("Instructions", help_menu, selection_color=(0, 0, 100))
game_menu.add_button('Exit', pygame_menu.events.EXIT)

game_menu.mainloop(screen)
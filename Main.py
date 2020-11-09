import pygame
#import pygame_menu
from pygame.locals import *

WIDTH = 800
HEIGHT = 800 

#COLOR PALLETE
BLACK = (0,0,0)
WHITE = (255,255,255)
#BLUE = (0,0,180)
GREY = (160,180,180)
#GREEN = (0,180,0)
YELLOW = (250,240,0)
#RED = (255,0,0)

#Creates vars for board size/color
FPS = 60
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
WIN.fill(GREY)
pygame.display.set_caption("Nine Men's Morris") #Window title


#MF axis font display
pygame.init() #initialize pygame to use fonts for text 
word_font = pygame.font.SysFont(None, 26)

#coordinates for placing board markers
axis = {"7": [70, 95], "6":[70, 195], "5":[70, 295], "4":[70, 395], "3":[70, 495], "2":[70, 595], "1":[70, 695],
        "a": [95, 720], "b":[195, 720], "c":[295, 720], "d":[395, 720], "e":[495, 720], "f":[595, 720], "g":[695, 720],}
for items in axis:
    text = word_font.render(items, True, (YELLOW))
    WIN.blit(text, axis[items])


#Function for creating Board
def make_board():
        color = BLACK
        board_coords1 = [600,400,200]
        board_coords2 = [100,200,300]
        spots = [] #cell coordinates list
        i = 0
        
        while i < 3:
            x = board_coords2[i]
            y = board_coords1[i]

            #setup circle placeholders
            pygame.draw.circle(WIN, color, (x,x), 5)
            spots.append([x,x])

            pygame.draw.circle(WIN, color, (y+x,y+x), 5)
            spots.append([y+x,y+x])

            pygame.draw.circle(WIN, color, (y+x,x), 5)
            spots.append([y+x,x])

            pygame.draw.circle(WIN, color, (x,y+x), 5)
            spots.append([x,y+x])

            pygame.draw.circle(WIN, color, (x, 400), 5)
            spots.append([x, 400])

            pygame.draw.circle(WIN, color, (y+x, 400), 5)
            spots.append([y+x, 400])

            pygame.draw.circle(WIN, color, (400, x), 5)
            spots.append([400, x])

            pygame.draw.circle(WIN, color, (400, x+y), 5)
            spots.append([400, x+y])
        
        
            #draws the long lines
            pygame.draw.line(WIN, color, (x,x), (x,y+x), 5)
            pygame.draw.line(WIN, color, (y+x,x), (y+x,y+x), 5)
            pygame.draw.line(WIN, color, (x,x), (y+x,x), 5)
            pygame.draw.line(WIN, color, (x,y+x), (y+x,y+x), 5)

            i=i+1
        
        #draws the short lines
        pygame.draw.line(WIN, color, (board_coords2[0],400), (board_coords2[2],400), 5) #a4 - c4
        pygame.draw.line(WIN, color, (board_coords2[0]+board_coords1[0],400), (board_coords2[2]+board_coords1[2],400), 5) #e4 - g4
        pygame.draw.line(WIN, color, (400,board_coords2[0]), (400,board_coords2[2]), 5) #d7 - d5
        pygame.draw.line(WIN, color, (400,board_coords2[0]+board_coords1[0]), (400,board_coords2[2]+board_coords1[2]), 5) #d3-d1
   
        pygame.display.flip()

        spots.sort() #sorts list of locations before the data goes into a dictionary 

        #makes a dictionary to number each spot location
        spots_Dict = {}
        for a, b in enumerate(spots): 
            spots_Dict[a] = b

        #print(spots_Dict)
        #Looks like {0: [100, 100], 1: [100, 400], 2: [100, 700], 3:[200,200]...}
        return spots_Dict

#Finding if mouse click is within the acceptable range of a coordinate to actually place piece
def Piece_Location(x, y, spots_Dict):
    xy_range = 25
    # Range set to 25, could be changed, seems good
    
    for i in spots_Dict.values():
        if (i[0] > x - xy_range and i[0] < x + xy_range and i[1] > y - xy_range and i[1] < y + xy_range):
            print(x, y, i[0], i[1])
            print("YEAH BOI") #Love it
            return [i[0],i[1]]
    else:
        return [0,0]
    
def cordsToNum(x, y, spots_Dict):
    for key, value in spots_Dict.items():
        if (value[0] == x and value[1] == y):
            return key

def isMill(placed_pieces, spots_dict):
    print(placed_pieces)
    mill_list = ((0,1,2), (3,4,5),(6,7,8),(9,10,11),(12,13,14),(15,16,17),(18,19,20),(21,22,23),(0,9,21),(3,10,18),(6,11,15),(1,4,7),(16,19,22),(8,12,17),
                 (5,13,20),(2,14,23))
    #pause()
    pass


def multiplayer():
    print("you've chosen to play with a friend")
    pass
def AI():
    print("You've chosen to play against the computer")
    pass
def rules():
    print("OooOOoOO we could list the rules here ig. whatcha guys think??")
    pass
def idek_mane(values, something):
    print("welp this is here too")
    pass

def menu():
    menu = pygame_menu.Menu(300, 400, "sup", theme=pygame_menu.themes.THEME_BLUE)
    menu.add_button("Play against friend", multiplayer)
    menu.add_button("Play against computer", AI)
    menu.add_button("View game rules", rules)
    menu.add_selector("select a thing", [("uwu", 1), ("rawr xD", 2)], onchange = idek_mane)
    menu.add_button("Quitter", pygame_menu.events.EXIT)
    menu.mainloop()


def main():

    #menu()

    turn = 1    #TRACK TURNS
    piece_countA = 0    #
    piece_countB = 0    #TRACK NO. PIECES
    taken_spots = []    #TRACK NON-AVAILABLE SPOTS
    black_placed = []
    white_placed = []

    #Possible_Mills = [[100, 100]] #creating mills going to be hard coz 

    run = True
    clock = pygame.time.Clock()

    while run:
        spots = make_board()
        clock.tick(FPS)
        #Test of make-board()
        #print("Board has been drawn")
        #return True
        
        #exits game on request
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            #search for user/mouse input
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()
                s, t = mouse_position
                [x, y] = Piece_Location(s, t, spots)
                location_num = cordsToNum(x, y, spots)

                #do nothing if spot is not available
                if [x, y] in taken_spots:
                    print ("----> Position not Empty <----")
                    continue

                #condition for if spot is available
                    #Test of taken_spots
                    #print("Piece has already been placed!")
                    pass
                
                #if spot is available
                else:
                    pygame.draw.rect(WIN, GREY, (650,50,120,20)) #erase and replace exiting text of text
                    
                    #keep total game pieces to 18, 9 for each player
                    if piece_countA == 9 and piece_countB == 9:
                        pass 

                    #condtions to determine player turns and player count
                    else:
                        #BLACK PLACEMENT
                        if turn % 2 == 0:
                            COLOR = BLACK
                            piece_countA += 1
                            text = fonzi.render("Turn: Player B", True, (YELLOW))
                            WIN.blit(text, [650,50])  

                        #WHITE PLACEMENT
                        else:
                            COLOR = WHITE
                            piece_countB += 1
                            text = fonzi.render ("Turn: Player A", True, (YELLOW))
                            WIN.blit(text, [650,50])  
                            
                            
                        #should this build be in seperate conditions above?
                        if [x,y] != [0,0]: 
                            pygame.draw.circle(WIN, BLACK, (x, y), 20)
                            pygame.draw.circle(WIN, COLOR, (x, y), 18)
                            if COLOR == BLACK:
                                pygame.draw.circle(WIN, BLACK, (x+5, y-3), 2)
                                black_placed.append(location_num)
                            else:
                                pygame.draw.circle(WIN, WHITE, (x+2, y-3), 2)
                                white_placed.append(location_num)

                            turn = turn + 1
                            taken_spots.append([x,y])
                            print("black spots:", black_placed)
                            print("white spots:", white_placed)

                
                #tESTS
                #print (x, y, s, t,"Here it is \n<----")
                #print (piece_countA, piece_countB)
                #print (taken_spots)

    pygame.quit()

#CALL THE ONLY FUNCTION
main()
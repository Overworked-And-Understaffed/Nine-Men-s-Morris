
import pygame

WIDTH = 800
HEIGHT = 800


#COLOR PALLETE
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,180)
GREY = (180,180,180)
GREEN = (0,180,0)
YELLOW = (255,255,0)
RED = (255,0,0)

FPS = 60
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
WIN.fill(GREY)

#MF axis font display
pygame.init() #initialize pygame to use fonts for text 
fonzi = pygame.font.SysFont(None, 26)
axis = {"M1": [20, 95], "M2":[20, 195], "M3":[20, 295], "M4":[20, 395], "M5":[20, 495], "M6":[20, 595], "M7":[20, 695],
        "F1": [95, 760], "F2":[195, 760], "F3":[295, 760], "F4":[395, 760], "F5":[495, 760], "F6":[595, 760], "F7":[695, 760],}
for mf in axis:
    text = fonzi.render(mf, True, (YELLOW))
    WIN.blit(text, axis[mf])

pygame.display.set_caption("Nine Men's Morris")

#Creates Board
def make_board():
        color = BLACK
        board_coords1 = [600,400,200]
        board_coords2 = [100,200,300]
        spots = [] #cell cordinates
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
        
        
            #draws the short lines
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

        spots.sort()

        spots_Dict = {}
        for a, b in enumerate(spots):
            spots_Dict[a] = b

        return spots_Dict
    
#Finding if mouse click is within the acceptable range of a coordinate to actually place piece
def Piece_Location(x, y, spots_Dict):
    xy_range = 25
    
    for i in spots_Dict.values():
        if (i[0] > x - xy_range and i[0] < x + xy_range and i[1] > y - xy_range and i[1] < y + xy_range):
            print(x, y, i[0], i[1])
            print("YEAH BOI") #Love it
            return [i[0],i[1]]
    else:
        return [0,0]

#def whos_turn():


def main():

    turn = 1    #TRACK TURNS
    piece_countA = 0    #
    piece_countB = 0    #TRACK NO. PIECES
    taken_spots = []    #TRACK NON-AVAILABLE SPOTS
    
    Possible_Mills = [[100, 100]] #creating mills going to be hard coz 

    run = True
    clock = pygame.time.Clock()

    while run:
        spots = make_board()
        clock.tick(FPS)
        
        #exits game on request
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()
                s, t = mouse_position
                [x, y] = Piece_Location(s, t, spots)

                #do nothing if spot is not available
                if [x, y] in taken_spots:
                    pass
                
                #if spot is available
                else:
                    #keep total piece to 18, 9 for each player
                    if piece_countA == 9 and piece_countB == 9:
                        pass ####
                    
                    else:
                        #BLACK PLACEMENT
                        if turn % 2 == 0:
                            COLOR = BLACK
                            piece_countA += 1   

                        #WHITE PLACEMENT
                        else:
                            COLOR = WHITE
                            piece_countB += 1
                        
                        #should this build be in seperate conditions above?
                        if [x,y] != [0,0]: 
                            pygame.draw.circle(WIN, BLACK, (x, y), 20)
                            pygame.draw.circle(WIN, COLOR, (x, y), 18)
                            turn = turn + 1
                            taken_spots.append([x,y])
                
                #tESTS
                #print (x, y, s, t,"Here it is \n<----")
                #print (piece_countA, piece_countB)
                #print (taken_spots)
             

    pygame.quit()

#CALL THE ONLY FUNCTION
main()


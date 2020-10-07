import pygame

WIDTH = 800
HEIGHT = 800


#not needed right now..?
#ROWS, COLS = 6, 6
#SQR_SIZE = WIDTH//COLS
#COLOR = (255,50,5)

#most arent in use. i think that "brown" is actually blue
WHITE = (255,255,255)
# BLUE = (200,0,2)
GREY = (180,180,180)
GREEN = (0,255,0)
YELLOW = (255,255,0)
RED = (0,0,0)



FPS = 60
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
WIN.fill(GREY)
pygame.display.set_caption("Nine Men's Morris")

#-----------------------------------------------------------!
def piece_creation(cordi_list, cordi_pos):
    for x,y in cordi_pos:
        if x or y in cordi_list:
            pygame.draw.circle(WIN, GREEN, (x,y), 20)
        
            #This is where I had enough and had to go to sleep...

        #-----------------------------------------------------------!
        #Remember to tell Elizabeth to expand list for additional tuples to pick from when 

                    
    
def main():
    run = True
    clock = pygame.time.Clock()
    cordi_set = [(100, 100), (100, 400), (100, 700),
                     (200, 200), (200, 400), (200, 600),
                     (400, 100), (400, 200), (400, 300),
                     (300, 300), (300, 400), (300, 500),
                     (400, 500), (400, 500), (400, 700),
                     (500, 300), (500, 400), (500, 500),
                     (600, 200), (600, 300), (600, 500),
                     (700, 100), (700, 400), (700, 700)]
    
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN: #"""DO CHECK HERE WHEN YOU GET THE CHANCE"""
                mouse_pos = pygame.mouse.get_pos()
                s, t = mouse_pos
                if s and t in cordi_set: 
                    pass           
                    #pygame.draw.circle(WIN, GREEN, (s, t), 20)
                pygame.draw.circle(WIN, RED, (s, t), 27)
                pygame.draw.circle(WIN, YELLOW, (s, t), 25)


        lens = [600,400,200]
        xy = [100,200,300]
        spots = []
        

        #-----------------------------------------------------------!
        # mouse_pos = pygame.mouse.get_pos()
        # mouse_click = pygame.mouse.get_pressed()
        # #print (mouse_pos)
        # s, t = mouse_pos
        # if mouse_click == True:
        #     print (s, t)
            
        #     #piece_creation(cordi_set, mouse_pos)
        #     pygame.draw.circle(WIN, GREEN, (s, t), 20)

        i = 0
        while i < 3:
            x = xy[i]
            y = lens[i]

            pygame.draw.circle(WIN, RED, (x,x), 10)
            spots.append([x,x])

            pygame.draw.circle(WIN, RED, (y+x,y+x), 10)
            spots.append([y+x,y+x])

            pygame.draw.circle(WIN, RED, (y+x,x), 10)
            spots.append([y+x,x])

            pygame.draw.circle(WIN, RED, (x,y+x), 10)
            spots.append([x,y+x])

            pygame.draw.circle(WIN, RED, (x, 400), 10)
            spots.append([x, 400])

            pygame.draw.circle(WIN, RED, (y+x, 400), 10)
            spots.append([y+x, 400])

            pygame.draw.circle(WIN, RED, (400, x), 10)
            spots.append([400, x])

            pygame.draw.circle(WIN, RED, (400, x+y), 10)
            spots.append([400, x+y])


            pygame.draw.line(WIN, RED, (x,x), (x,y+x), 10)
            pygame.draw.line(WIN, RED, (y+x,x), (y+x,y+x), 10)
            pygame.draw.line(WIN, RED, (x,x), (y+x,x), 10)
            pygame.draw.line(WIN, RED, (x,y+x), (y+x,y+x), 10)

            i=i+1
        
        #draws the short lines
        pygame.draw.line(WIN, RED, (xy[0],400), (xy[2],400), 10) #a4 - c4
        pygame.draw.line(WIN, RED, (xy[0]+lens[0],400), (xy[2]+lens[2],400), 10) #e4 - g4
        pygame.draw.line(WIN, RED, (400,xy[0]), (400,xy[2]), 10) #d7 - d5
        pygame.draw.line(WIN, RED, (400,xy[0]+lens[0]), (400,xy[2]+lens[2]), 10) #d3-d1

       
        
        pygame.display.flip()
    
    #shows the X Y locations of each spot    
    print(spots)
    print(len(spots))

    #confirmed theres no duplicates, we could delete this
    res = []
    for i in spots: 
        if i not in res: 
            res.append(i) 

    print(res)
    print(len(spots))

    #so I guess we want to translate this to something like [spot number : spot location] ? whatcha think??

    pygame.quit()

main()

""" 
import pygame, sys
from pygame.locals import *

def main():
    pygame.init()

    DISPLAY = pygame.display.set_mode((800,800),0,32) #(length, width, x, y)
    pygame.display.set_caption("Nine Men's Morris")

    WHITE = (255,255,255)
    BLUE = (200,0,2)
    BROWN = (0,175,226)
    GREEN = (45, 234, 65)
    PURPLE = (100, 34, 165)
    RED = (255, 0, 0)

    DISPLAY.fill(BROWN)

    pygame.draw.rect(DISPLAY,WHITE,(80,80,600,600)) #(x, y, length, width)
    pygame.draw.rect(DISPLAY,GREEN,(160,160,400,400)) #(x, y, length, width)
    pygame.draw.rect(DISPLAY,PURPLE,(260,260,200,200)) #(x, y, length, width)
    
    pygame.draw.circle(DISPLAY, RED, (80,80), 10)
    #pygame.draw.line(DISPLAY, RED, 80, 160, 10)# -> Rect
    
    
    while True:
        for event in pygame.event.get():
            if event.type==QUIT:
                #pygame.quit()
                sys.exit()
        pygame.display.update()

main()
 """

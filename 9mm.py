
import pygame

WIDTH = 800
HEIGHT = 800

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
pygame.display.set_caption("Nine Men's Morris")


def make_board():
        color = BLACK
        lens = [600,400,200]
        xy = [100,200,300]
        spots = []
        i = 0
        while i < 3:
            x = xy[i]
            y = lens[i]


            pygame.draw.circle(WIN, color, (x,x), 10)
            spots.append([x,x])

            pygame.draw.circle(WIN, color, (y+x,y+x), 10)
            spots.append([y+x,y+x])

            pygame.draw.circle(WIN, color, (y+x,x), 10)
            spots.append([y+x,x])

            pygame.draw.circle(WIN, color, (x,y+x), 10)
            spots.append([x,y+x])

            pygame.draw.circle(WIN, color, (x, 400), 10)
            spots.append([x, 400])

            pygame.draw.circle(WIN, color, (y+x, 400), 10)
            spots.append([y+x, 400])

            pygame.draw.circle(WIN, color, (400, x), 10)
            spots.append([400, x])

            pygame.draw.circle(WIN, color, (400, x+y), 10)
            spots.append([400, x+y])


            pygame.draw.line(WIN, color, (x,x), (x,y+x), 10)
            pygame.draw.line(WIN, color, (y+x,x), (y+x,y+x), 10)
            pygame.draw.line(WIN, color, (x,x), (y+x,x), 10)
            pygame.draw.line(WIN, color, (x,y+x), (y+x,y+x), 10)

            i=i+1
        
        #draws the short lines
        pygame.draw.line(WIN, color, (xy[0],400), (xy[2],400), 10) #a4 - c4
        pygame.draw.line(WIN, color, (xy[0]+lens[0],400), (xy[2]+lens[2],400), 10) #e4 - g4
        pygame.draw.line(WIN, color, (400,xy[0]), (400,xy[2]), 10) #d7 - d5
        pygame.draw.line(WIN, color, (400,xy[0]+lens[0]), (400,xy[2]+lens[2]), 10) #d3-d1
   
        pygame.display.flip()

        spots.sort()

        spots_Dict = {}
        for a, b in enumerate(spots):
            spots_Dict[a] = b

        return spots_Dict
    

def check_pos(x, y, spots_Dict):
    xy_range = 25
    for i in spots_Dict.values():
        if (i[0] > x - xy_range and i[0] < x + xy_range and i[1] > y - xy_range and i[1] < y + xy_range):
            print(x, y, i[0], i[1])
            print("YEAH BOI")
            return [i[0],i[1]]
    else:
        return [0,0]

#def whos_turn():


def main():

    turn = 1

    run = True
    clock = pygame.time.Clock()

    while run:
        spots = make_board()
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                s, t = mouse_pos
                [x, y] = check_pos(s, t, spots)

                if turn % 2 == 0:
                    COLOR = BLUE
                else:
                    COLOR = GREEN
                
                if [x,y] != [0,0]:
                    pygame.draw.circle(WIN, COLOR, (x, y), 25)
                    turn = turn + 1

    pygame.quit()

main()


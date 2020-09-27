import pygame

WIDTH = 800
HEIGHT = 800

#not needed right now..?
#ROWS, COLS = 6, 6
#SQR_SIZE = WIDTH//COLS
#COLOR = (255,50,5)

#most arent in use. i think that "brown" is actually blue
WHITE = (255,255,255)
BLUE = (200,0,2)
BROWN = (0,175,226)
GREEN = (45, 234, 65)
PURPLE = (100, 34, 165)
RED = (255, 0, 0)

FPS = 60
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Nine Men's Morris")

def main():
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass


        WIN.fill(BROWN)

        lens = [600,400,200]
        xy = [100,200,300]
        spots = []

        i = 0
        while i < 3:
            x = xy[i]
            y = lens[i]

            pygame.draw.circle(WIN, RED, (x,x), 30)
            spots.append([x,x])

            pygame.draw.circle(WIN, RED, (y+x,y+x), 30)
            spots.append([y+x,y+x])

            pygame.draw.circle(WIN, RED, (y+x,x), 30)
            spots.append([y+x,x])

            pygame.draw.circle(WIN, RED, (x,y+x), 30)
            spots.append([x,y+x])

            pygame.draw.circle(WIN, RED, (x, 400), 30)
            spots.append([x, 400])

            pygame.draw.circle(WIN, RED, (y+x, 400), 30)
            spots.append([y+x, 400])

            pygame.draw.circle(WIN, RED, (400, x), 30)
            spots.append([400, x])

            pygame.draw.circle(WIN, RED, (400, x+y), 30)
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

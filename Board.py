
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
    
    pygame.draw.circle(DISPLAY, RED, (80,80), 30)
    #pygame.draw.line(DISPLAY, RED, 80, 160, 10)# -> Rect
    
    
    while True:
        for event in pygame.event.get():
            if event.type==QUIT:
                #pygame.quit()
                sys.exit()
        pygame.display.update()

main()
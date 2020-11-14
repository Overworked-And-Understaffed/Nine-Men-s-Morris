import pygame
import pygame_menu

color = [128, 128, 50]
pygame.init()
surface = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Nine Men's Morris")
surface.fill(color)
def game_instructions():
    
    pass

def start_the_game():
    # Do the job here !
    pass


menu = pygame_menu.Menu(300, 400, "Menu", theme=pygame_menu.themes.THEME_SOLARIZED)

menu.add_label("Nine Men's Morris Game")
#menu.add_selector('Difficulty :', [('Hard', 1), ('Easy', 2)], onchange=set_difficulty)
menu.add_button('Play', start_the_game)
menu.add_button("Instructions", game_instructions)
menu.add_button('Quit', pygame_menu.events.EXIT)

menu.mainloop(surface)
    
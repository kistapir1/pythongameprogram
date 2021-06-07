import pygame
import pygame_menu
#import jatek

pygame.init()
surface = pygame.display.set_mode((800, 600))

def start_the_game():

    pass

menu = pygame_menu.Menu(width = 600, height = 450, title = 'Welcome',
                       theme=pygame_menu.themes.THEME_BLUE)

menu.add.button('Play', start_the_game)
menu.add.button('Quit', pygame_menu.events.EXIT)

menu.mainloop(surface)
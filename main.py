import pygame
from constants import *
from screens.game import Game
from screens.menu import Menu

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
active_screen = 0
run = True
while run:
    if active_screen == 0: # MENU
        window_instance = Menu(screen)
        active_screen = window_instance.loop()
    if active_screen == 1: # GAME / BOT
        window_instance = Game(screen, 'pve')
        active_screen = window_instance.loop()
    if active_screen == 2: # GAME / MULTIPLAYER
        window_instance = Game(screen, 'pvp')
        active_screen = window_instance.loop()
    
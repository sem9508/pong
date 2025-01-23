import pygame
from constants import *
from objects.button import *


# 303030
class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.run = True
        self.clock = pygame.time.Clock()
        pygame.display.set_caption('Menu')
        self.singleplayer_btn = Button(self.screen.get_width()/2-300/2, 50, 300, 100, 'assets/images/Singleplayer.png') # deze is 300 bij 100
        self.multiplayer_btn = Button(self.screen.get_width()/2-300/2, 165, 300, 100, 'assets/images/Multiplayer.png') # deze is 300 bij 100
        self.next_screen = None

    def loop(self):
        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.singleplayer_btn.update(pygame.mouse.get_pos()):
                        self.run = False
                        self.next_screen = 1 # normal game

                    elif self.multiplayer_btn.update(pygame.mouse.get_pos()):
                        self.run = False
                        self.next_screen = 2

            self.screen.fill(BLACK)
            self.singleplayer_btn.draw(self.screen)
            self.multiplayer_btn.draw(self.screen)
            pygame.display.update()
            self.clock.tick(FPS)

        return self.next_screen

import pygame
from constants import *
from objects.button import *

class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.run = True
        self.clock = pygame.time.Clock()
        pygame.display.set_caption('Menu')
        self.start_btn = Button(self.screen.get_width()/2-300/2, 50, 300, 100, 'assets/images/start.png') # deze is 300 bij 100
        self.next_screen = None

    def loop(self):
        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.start_btn.update(pygame.mouse.get_pos()):
                        self.run = False
                        self.next_screen = 1 # normal game

            self.screen.fill(BLACK)
            self.start_btn.draw(self.screen)
            pygame.display.update()
            self.clock.tick(FPS)

        return self.next_screen
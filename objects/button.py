import pygame
from constants import WHITE

class Button:
    def __init__(self, x, y, width, height, path):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.image = pygame.image.load(path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (width, height))


    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def update(self, mouse):
        if self.rect.collidepoint(mouse[0], mouse[1]):
            return True
        else:
            return False
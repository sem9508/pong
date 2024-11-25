import pygame
from utils import *
from physicsobject import *

class Paddle(PhysicsObject):
    def __init__(self, x, y_mid, width, height, max_speed, acceleration_spd, color, input_group, game_manager):
        super().__init__(x, y_mid, width, height, max_speed, acceleration_spd)
        self.color = color
        self.input_group = input_group
        self.game_manager = game_manager
        self.key_pressed_x = False
        self.key_pressed_y = False

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    def update(self):
        if self.key_pressed_y == False:
            self.set_acceleration([self.acceleration[0], 0])
            self.velocity[1] /= self.resistance_factor
        if self.key_pressed_x == False:
            self.set_acceleration([0, self.acceleration[1]])
            self.velocity[0] /= self.resistance_factor
        
        self.update_pos()

        if self.rect.y < 0:
            self.rect.y = 0
        elif self.rect.y > self.game_manager.screen_height - self.height:
            self.rect.y = self.game_manager.screen_height - self.height
            
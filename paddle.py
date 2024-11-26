import pygame
from utils import *
from objects import *

class Paddle(PhysicsObject):
    def __init__(self, x, y_mid, width, height, max_speed, acceleration_spd, color, input_group, game_manager, particle_color):
        super().__init__(x, y_mid, width, height, max_speed, acceleration_spd)
        self.color = color
        self.input_group = input_group
        self.game_manager = game_manager
        self.key_pressed_x = False
        self.key_pressed_y = False

        self.particle = ParticleObject(particle_color, 1, 15, self.rect.width/2, 2)

    def draw(self, screen):
        self.particle.draw(screen)
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

        self.particle.update((self.rect.x+self.rect.width/2, self.rect.y+self.rect.height/2))
            
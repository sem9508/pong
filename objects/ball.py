import pygame
from utils import *
from components.physicsobject import *
import random
from components.particleobject import *

from constants import *


class Ball(PhysicsObject):
    def __init__(self, x, y_mid, width, height, max_speed, acceleration_spd, color, radius, start_vel_vector, game_manager, BALL_SPD_INCREMENT):
        super().__init__(x, y_mid, width, height, max_speed, acceleration_spd)

        self.color = color
        self.radius = radius
        self.center = (x + width/2, y_mid)
        self.velocity = start_vel_vector
        self.ball_speed_increment = BALL_SPD_INCREMENT
        self.game_manager = game_manager

        self.particle = ParticleObject((33, 200, 153), 1, 15, self.radius, 0.1)

    def draw(self, screen):
        self.particle.draw(screen)
        pygame.draw.circle(screen, self.color, self.center, self.radius)

    def update(self):
        self.update_pos()
        for obj in self.game_manager.collision_objects:
            if obj == self:
                continue
            else:
                if self.rect.colliderect(obj):
                    self.velocity[0] *= -1
                    self.velocity[1] = random.randrange(-100, 100)/100
                    self.max_speed += self.ball_speed_increment

        if self.rect.y > self.game_manager.screen_height or self.rect.y < 0:
            self.velocity[1] *= -1
        if self.rect.x < 0:
            self.game_manager.point_scored(0)
            self.ball_speed_increment = BALL_SPD_INCREMENT
            self.max_speed = STD_MAX_BALL_SPD
        elif self.rect.x > self.game_manager.screen_width:
            self.game_manager.point_scored(1)
            self.ball_speed_increment = BALL_SPD_INCREMENT
            self.max_speed = STD_MAX_BALL_SPD

        self.center = (self.rect.x, self.rect.y)

        self.particle.update(self.center)

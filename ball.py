import pygame
from utils import *
from physicsobject import *
import random


class Ball(PhysicsObject):
    def __init__(self, x, y_mid, width, height, max_speed, acceleration_spd, color, radius, start_vel_vector, game_manager, BALL_SPD_INCREMENT):
        super().__init__(x, y_mid, width, height, max_speed, acceleration_spd)

        self.color = color
        self.radius = radius
        self.center = (x + width/2, y_mid)
        self.velocity = start_vel_vector
        self.ball_speed_increment = BALL_SPD_INCREMENT
        self.game_manager = game_manager

        self.trail = [(-10, -10)]
        self.trail_timer = 0
        self.trail_interval = 1
        self.trail_length = 10
        self.max_size = 5
        self.min_size = 1

    def draw(self, screen):
        for i in range(len(self.trail)):
            if len(self.trail) > 1:
                size = self.min_size + (i / (len(self.trail) - 1)) * (self.max_size - self.min_size)
            else:
                size = self.max_size  # If there's only one particle, it should be the max size
            pygame.draw.circle(screen, (48, 40, 80), self.trail[i], size)
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
        elif self.rect.x > self.game_manager.screen_width:
            self.game_manager.point_scored(1)
        self.center = (self.rect.x, self.rect.y)

        if self.trail_timer > self.trail_interval:
            self.trail_timer = 0
            self.trail.append(self.center)
            if len(self.trail) > self.trail_length:
                self.trail.pop(0)
        else:
            self.trail_timer += 1
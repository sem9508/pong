import pygame
from utils import *
from physicsobject import *


class Ball(PhysicsObject):
    def __init__(self, x, y_mid, width, height, max_speed, acceleration_spd, color, radius, start_vel_vector, game_manager):
        super().__init__(x, y_mid, width, height, max_speed, acceleration_spd)

        self.color = color
        self.radius = radius
        self.center = (x + width/2, y_mid)
        self.velocity = start_vel_vector

        self.game_manager = game_manager

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.center, self.radius)

    def update(self):
        self.update_pos()
        for obj in self.game_manager.collision_objects:
            if obj == self:
                continue
            else:
                if self.rect.colliderect(obj):
                    # Check if the ball is moving towards the paddle (left or right)
                    if self.velocity[0] == -1 and self.rect.x + self.rect.width > obj.rect.x and self.rect.x < obj.rect.x + obj.rect.width:
                        # Ball is moving left and collides with the paddle
                        self.velocity[0] *= -1  # Reverse the velocity
                        self.rect.x = obj.rect.x + obj.rect.width  # Move the ball just after the paddle

                    elif self.velocity[0] == 1 and self.rect.x < obj.rect.x + obj.rect.width and self.rect.x + self.rect.width > obj.rect.x:
                        # Ball is moving right and collides with the paddle
                        self.velocity[0] *= -1  # Reverse the velocity
                        self.rect.x = obj.rect.x - self.rect.width  # Move the ball just before the paddle

                        

        if self.rect.y > self.game_manager.screen_height or self.rect.y < 0:
            self.velocity[1] *= -1
        if self.rect.x < 0:
            self.game_manager.point_scored(0)
        elif self.rect.x > self.game_manager.screen_width:
            self.game_manager.point_scored(1)
        self.center = (self.rect.x, self.rect.y)
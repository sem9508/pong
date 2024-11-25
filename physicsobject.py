import pygame
from utils import *

class PhysicsObject:
    def __init__(self, x, y_mid, width, height, max_speed, acceleration_spd) -> None:
        self.width = width
        self.height = height
        self.max_speed = max_speed
        self.acceleration_spd = acceleration_spd
        self.velocity = [0, 0]
        self.acceleration = [0, 0]
        self.resistance_factor = 1.08
        self.rect = pygame.Rect(x, y_mid-height/2, self.width, self.height)

    def set_velocity(self, vector):
        vector = check_max_vector(vector)
        self.velocity = vector

    def add_velocity(self, vector):
        self.velocity[0] += vector[0]
        self.velocity[1] += vector[1]
        self.velocity = check_max_vector(self.velocity)

    def set_acceleration(self, vector):
        vector = check_max_vector(vector)
        self.acceleration = vector

    def add_acceleration(self, vector):
        self.acceleration[0] += vector[0]
        self.acceleration[1] += vector[1]
        self.acceleration = check_max_vector(self.acceleration)

    def update_pos(self):
        self.add_velocity(self.acceleration)

        if abs(self.velocity[0]) <= 0.05:
            self.velocity[0] = 0
        if abs(self.velocity[1]) <= 0.05:
            self.velocity[1] = 0

        self.rect.x += self.velocity[0] * self.max_speed
        self.rect.y += self.velocity[1] * self.max_speed


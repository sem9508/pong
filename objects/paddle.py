import pygame
from utils import *
from components.particleobject import *
from components.physicsobject import *
from objects.ball import *

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
        if not self.key_pressed_y:
            self.set_acceleration([self.acceleration[0], 0])
            self.velocity[1] /= self.resistance_factor
        if not self.key_pressed_x:
            self.set_acceleration([0, self.acceleration[1]])
            self.velocity[0] /= self.resistance_factor
        
        self.update_pos()

        if self.rect.y < 0:
            self.rect.y = 0
        elif self.rect.y > self.game_manager.screen_height - self.height:
            self.rect.y = self.game_manager.screen_height - self.height

        self.particle.update((self.rect.x+self.rect.width/2, self.rect.y+self.rect.height/2))

class Paddle_ai(PhysicsObject):
    def __init__(self, x, y_mid, width, height, max_speed, acceleration_spd, color, input_group, game_manager, particle_color):
        super().__init__(x, y_mid, width, height, max_speed, acceleration_spd)
        self.color = color
        self.input_group = input_group
        self.game_manager = game_manager
        self.x_moving = False
        self.y_moving = False

        self.particle = ParticleObject(particle_color, 1, 15, self.rect.width / 2, 2)

    def draw(self, screen):
        self.particle.draw(screen)
        pygame.draw.rect(screen, self.color, self.rect)

    def update(self):
        for obj in self.game_manager.collision_objects:
            if type(obj) == Ball:
                ball_to_track = obj

        if ball_to_track.center[1] > self.rect.y+self.rect.height - self.height/5:
            self.add_velocity([0, self.max_speed])
            self.y_moving = True
        elif ball_to_track.center[1] < self.rect.y+ self.height/5:
            self.add_velocity([0, -self.max_speed])
            self.y_moving = True
        elif ball_to_track.center[1] > self.rect.y+ self.height/5 and ball_to_track.center[1] < self.rect.y+self.rect.height- self.height/5:
            self.y_moving = False

        if not self.y_moving:
            self.set_acceleration([self.acceleration[0], 0])
            self.velocity[1] /= self.resistance_factor
        if not self.x_moving:
            self.set_acceleration([0, self.acceleration[1]])
            self.velocity[0] /= self.resistance_factor

        self.update_pos()


        if self.rect.y < 0:
            self.rect.y = 0
        elif self.rect.y > self.game_manager.screen_height - self.height:
            self.rect.y = self.game_manager.screen_height - self.height

        self.particle.update((self.rect.x + self.rect.width / 2, self.rect.y + self.rect.height / 2))

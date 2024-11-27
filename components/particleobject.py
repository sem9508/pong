import pygame

class ParticleObject:
    def __init__(self, color, trail_interval, trail_length, max_size, min_size) -> None:
        self.trail = []
        self.color = color
        self.trail_timer = 0
        self.trail_interval = trail_interval
        self.trail_length = trail_length
        self.max_size = max_size
        self.min_size = min_size

    def update(self, newPos):
        if self.trail_timer > self.trail_interval:
            self.trail_timer = 0
            self.trail.append(newPos)
            if len(self.trail) > self.trail_length:
                self.trail.pop(0)
        else:
            self.trail_timer += 1

    def draw(self, screen):
        for i in range(len(self.trail)):
            if len(self.trail) > 1:
                size = self.min_size + (i / (len(self.trail) - 1)) * (self.max_size - self.min_size)
            else:
                size = self.max_size  # If there's only one particle, it should be the max size
            pygame.draw.circle(screen, self.color, self.trail[i], size)

    def update_color(self, color):
        self.color = color
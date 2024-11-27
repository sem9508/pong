import random
from objects.ball import Ball


class GameManager:
    def __init__(self, screen_width, screen_height):
        self.collision_objects = []
        self.objects = []
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.score = [0, 0]

    def add_collision_object(self, obj):
        self.collision_objects.append(obj)

    def add_game_object(self, obj):
        self.objects.append(obj)

    def reset(self):
        ball = next(obj for obj in self.objects if isinstance(obj, Ball))
        ball.velocity[0] = random.choice([-1, 1])
        ball.velocity[1] = random.randrange(-100, 100)/100
        ball.rect.x = self.screen_width/2-ball.width/2
        ball.rect.y = self.screen_height/2-ball.height/2

    def point_scored(self, team):
        self.score[team] += 1
        self.reset()

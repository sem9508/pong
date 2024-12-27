import pygame
import time
import random
import sys
from objects.paddle import *
from managers.input_manager import *
from utils import *
from objects.ball import *
from managers.game_manager import GameManager
from constants import *
from managers.music_manager import *


class Game:
    def __init__(self, screen):
        self.font = pygame.font.SysFont('Stencil', 74)

        self.game_manager = GameManager(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.music_manager = MusicManager('assets\sound\music.ogg', 3000)

        # VARIABLES
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.run = True

        self.player_paddle = Paddle(PADDLE_OFFSET_X, SCREEN_HEIGHT/2, STD_PADDLE_WIDTH, STD_PADDLE_HEIGHT, STD_MAX_PADDLE_SPEED, STD_ACCELERATION_SPD, WHITE, 1, self.game_manager, BLUE)
        self.enemy_paddle = Paddle_ai(SCREEN_WIDTH-PADDLE_OFFSET_X-STD_PADDLE_WIDTH, SCREEN_HEIGHT/2, STD_PADDLE_WIDTH, STD_PADDLE_HEIGHT, STD_MAX_PADDLE_SPEED, STD_ACCELERATION_SPD, WHITE, None, self.game_manager, RED)
        self.ball = Ball(SCREEN_WIDTH/2-STD_BALL_WIDTH/2, SCREEN_HEIGHT/2, STD_BALL_WIDTH, STD_BALL_HEIGHT, STD_MAX_BALL_SPD, STD_ACCELERATION_SPD, WHITE, STD_BALL_RADIUS, [random.choice([-1, 1]), random.randrange(-100, 100)/100], self.game_manager, BALL_SPD_INCREMENT)


        self.game_manager.objects.append(self.player_paddle)
        self.game_manager.objects.append(self.enemy_paddle)
        self.game_manager.objects.append(self.ball)

        self.game_manager.collision_objects.append(self.player_paddle)
        self.game_manager.collision_objects.append(self.enemy_paddle)
        self.game_manager.collision_objects.append(self.ball)

        self.music_manager.play(0)

    def loop(self):
        while self.run:
            # INPUT
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                    sys.exit()
            
            keys = pygame.key.get_pressed()
            objects = use_input(keys, self.game_manager.objects)

            # UPDATES
            for obj in objects:
                obj.update()

            # DRAWING
            self.screen.fill(BLACK)
            draw_dotted_line(self.screen, WHITE, (SCREEN_WIDTH/2-1, 0), (SCREEN_WIDTH/2, SCREEN_HEIGHT), 2, 10)
            for obj in objects:
                obj.draw(self.screen)

            text_surface = self.font.render(str(self.game_manager.score[1]) + '        ' + str(self.game_manager.score[0]), True, (255, 255, 255))
            self.screen.blit(text_surface, (SCREEN_WIDTH/2-text_surface.get_width()/2, 50))

            # MUSIC
            self.music_manager.fade_update()

            pygame.display.flip()
            self.clock.tick(FPS)
            pygame.display.set_caption("FPS: " + str(int(self.clock.get_fps())))



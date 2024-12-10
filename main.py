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

# INITIALIZATION
pygame.init()
pygame.mixer.init()
game_manager = GameManager(SCREEN_WIDTH, SCREEN_HEIGHT)
music_manager = MusicManager('assets\sound\music.ogg', 3000)

# VARIABLES
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
run = True

player_paddle = Paddle(PADDLE_OFFSET_X, SCREEN_HEIGHT/2, STD_PADDLE_WIDTH, STD_PADDLE_HEIGHT, STD_MAX_PADDLE_SPEED, STD_ACCELERATION_SPD, WHITE, 1, game_manager, BLUE)
enemy_paddle = Paddle_ai(SCREEN_WIDTH-PADDLE_OFFSET_X-STD_PADDLE_WIDTH, SCREEN_HEIGHT/2, STD_PADDLE_WIDTH, STD_PADDLE_HEIGHT, STD_MAX_PADDLE_SPEED, STD_ACCELERATION_SPD, WHITE, None, game_manager, RED)
ball = Ball(SCREEN_WIDTH/2-STD_BALL_WIDTH/2, SCREEN_HEIGHT/2, STD_BALL_WIDTH, STD_BALL_HEIGHT, STD_MAX_BALL_SPD, STD_ACCELERATION_SPD, WHITE, STD_BALL_RADIUS, [random.choice([-1, 1]), random.randrange(-100, 100)/100], game_manager, BALL_SPD_INCREMENT)

game_manager.objects.append(player_paddle)
game_manager.objects.append(enemy_paddle)
game_manager.objects.append(ball)

game_manager.collision_objects.append(player_paddle)
game_manager.collision_objects.append(enemy_paddle)
game_manager.collision_objects.append(ball)

music_manager.play(0)
# GAME LOOP
while run:
    # INPUT
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break
    
    keys = pygame.key.get_pressed()
    objects = use_input(keys, game_manager.objects)

    # UPDATES
    for obj in objects:
        obj.update()

    # DRAWING
    screen.fill(BLACK)
    draw_dotted_line(screen, WHITE, (SCREEN_WIDTH/2-1, 0), (SCREEN_WIDTH/2, SCREEN_HEIGHT), 2, 10)
    for obj in objects:
        obj.draw(screen)

    # MUSIC
    music_manager.fade_update()

    # END OF FRAME
    pygame.display.flip()
    clock.tick(FPS)
    pygame.display.set_caption("FPS: " + str(int(clock.get_fps())))


pygame.quit()
sys.exit()

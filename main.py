import pygame
import time
import random
import sys
from paddle import *
from input_manager import *
from utils import *
from ball import *
from game_manager import GameManager

# INITIALIZATION
pygame.init()

# CONSTANTS
SCREEN_WIDTH = 750
SCREEN_HEIGHT = 600

PADDLE_OFFSET_X = 10
STD_PADDLE_WIDTH = 10
STD_PADDLE_HEIGHT = 70
STD_MAX_PADDLE_SPEED = 5
STD_ACCELERATION_SPD = 0.1

STD_BALL_RADIUS = 4
STD_BALL_WIDTH = STD_BALL_RADIUS
STD_BALL_HEIGHT = STD_BALL_RADIUS
STD_MAX_BALL_SPD = 2

BALL_SPD_INCREMENT = 0.1

FPS = 80

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# MANAGERS
game_manager = GameManager(SCREEN_WIDTH, SCREEN_HEIGHT)

# VARIABLES
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
run = True

player_paddle = Paddle(PADDLE_OFFSET_X, SCREEN_HEIGHT/2, STD_PADDLE_WIDTH, STD_PADDLE_HEIGHT, STD_MAX_PADDLE_SPEED, STD_ACCELERATION_SPD, WHITE, 1, game_manager)
enemy_paddle = Paddle(SCREEN_WIDTH-PADDLE_OFFSET_X-STD_PADDLE_WIDTH, SCREEN_HEIGHT/2, STD_PADDLE_WIDTH, STD_PADDLE_HEIGHT, STD_MAX_PADDLE_SPEED, STD_ACCELERATION_SPD, WHITE, 2, game_manager)
ball = Ball(SCREEN_WIDTH/2-STD_BALL_WIDTH/2, SCREEN_HEIGHT/2, STD_BALL_WIDTH, STD_BALL_HEIGHT, STD_MAX_BALL_SPD, STD_ACCELERATION_SPD, WHITE, STD_BALL_RADIUS, [random.choice([-1, 1]), random.randrange(-100, 100)/100], game_manager, BALL_SPD_INCREMENT)

game_manager.objects.append(player_paddle)
game_manager.objects.append(enemy_paddle)
game_manager.objects.append(ball)

game_manager.collision_objects.append(player_paddle)
game_manager.collision_objects.append(enemy_paddle)
game_manager.collision_objects.append(ball)
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

    # END OF FRAME
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()

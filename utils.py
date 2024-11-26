import pygame

def check_max_vector(vector):
    if vector[0] > 1:
        vector[0] = 1
    if vector[0] < -1:
        vector[0] = -1
    if vector[1] > 1:
        vector[1] = 1 
    if vector[1] < -1:
        vector[1] = -1

    return vector 

def draw_dotted_line(screen, color, start_pos, end_pos, width=1, dash_length=10):
    x1, y1 = start_pos
    x2, y2 = end_pos
    dx = x2 - x1
    dy = y2 - y1
    gab = 10
    distance = max(abs(dx), abs(dy))
    steps = int(distance / (dash_length + gab))

    for i in range(steps + 1):
        x = x1 + dx * i / steps
        y = y1 + dy * i / steps
        pygame.draw.line(screen, color, (x, y), (x, y+ dash_length), width)
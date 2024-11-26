import pygame

def handle_movement(keys, obj, up_key, down_key, x_movement_active=False, left_key=None, right_key=None):
    obj.key_pressed_x = False
    obj.key_pressed_y = False

    if keys[up_key]:
        obj.add_acceleration([0, -obj.acceleration_spd])
        obj.key_pressed_y = True
    if keys[down_key]:
        obj.add_acceleration([0, obj.acceleration_spd])
        obj.key_pressed_y = True
    if keys[up_key] and keys[down_key]:
        obj.key_pressed_y = False

    if left_key and right_key and x_movement_active:
        if keys[right_key]:
            obj.add_acceleration([obj.acceleration_spd, 0])
            obj.key_pressed_x = True
        if keys[left_key]:
            obj.add_acceleration([-obj.acceleration_spd, 0])
            obj.key_pressed_x = True
        if keys[right_key] and keys[left_key]:
            obj.key_pressed_x = False

def use_input(keys, objects):
    for obj in objects:
        if hasattr(obj, 'input_group'):
            if obj.input_group == 1:
                handle_movement(keys, obj, pygame.K_w, pygame.K_s, False, pygame.K_a, pygame.K_d)
            elif obj.input_group == 2:
                handle_movement(keys, obj, pygame.K_UP, pygame.K_DOWN, False, pygame.K_LEFT, pygame.K_RIGHT)
    
    return objects

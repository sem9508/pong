import pygame


def use_input(keys, objects):
    for obj in objects:
        if hasattr(obj, 'input_group'):
            if obj.input_group == 1:
                obj.key_pressed_x = False
                obj.key_pressed_y = False
                if keys[pygame.K_w]:
                    obj.add_acceleration([0, -obj.acceleration_spd])
                    obj.key_pressed_y = True
                if keys[pygame.K_s]:
                    obj.add_acceleration([0, obj.acceleration_spd])
                    obj.key_pressed_y = True
                '''
                if keys[pygame.K_d]:
                    obj.add_acceleration([obj.acceleration_spd, 0])
                    obj.key_pressed_x = True
                if keys[pygame.K_a]:
                    obj.add_acceleration([-obj.acceleration_spd, 0])
                    obj.key_pressed_x = True
                '''
                if keys[pygame.K_w] and keys[pygame.K_s]:
                    obj.key_pressed_y = False
                if keys[pygame.K_d] and keys[pygame.K_a]:
                    obj.key_pressed_x = False

            elif obj.input_group == 2:
                obj.key_pressed_x = False
                obj.key_pressed_y = False
                if keys[pygame.K_UP]:
                    obj.add_acceleration([0, -obj.acceleration_spd])
                    obj.key_pressed_y = True
                if keys[pygame.K_DOWN]:
                    obj.add_acceleration([0, obj.acceleration_spd])
                    obj.key_pressed_y = True
                '''
                if keys[pygame.K_RIGHT]:
                    obj.add_acceleration([obj.acceleration_spd, 0])
                    obj.key_pressed_x = True
                if keys[pygame.K_LEFT]:
                    obj.add_acceleration([-obj.acceleration_spd, 0])
                    obj.key_pressed_x = True
                '''
                if keys[pygame.K_UP] and keys[pygame.K_DOWN]:
                    obj.key_pressed_y = False
                if keys[pygame.K_RIGHT] and keys[pygame.K_LEFT]:
                    obj.key_pressed_x = False

    return objects
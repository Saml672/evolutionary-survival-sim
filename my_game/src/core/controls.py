"""
Zoom in and out: We need to modify the screen positions
"""
import pygame
def game_controls(world):

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        if event.type == pygame.MOUSEBUTTONDOWN:
            # grabbing starting position from click

            world.mouse_current_pos = world.mouse_position()
            world.mouse_new_pos = world.mouse_current_pos
            # print(world.mouse_current_pos)
    if pygame.mouse.get_pressed()[0] == True:
        world.mouse_current_pos = world.mouse_position()
        
        
            
            
            

    return True
import pygame
class World:
    camera = [0,0]
    width = 1280
    height = 720
    half_width = width / 2
    half_height = height / 2
    def __init__(self):
        self.WORLD_WIDTH = 5000
        self.WORLD_HEIGHT = 5000
        self.mouse_current_pos = (0,0)
        self.mouse_new_pos = (0,0)

    def mouse_position(self):
        self.mouse_pos_x, self.mouse_pos_y = pygame.mouse.get_pos()
        return self.mouse_pos_x,self.mouse_pos_y
    def move_camera(self):


        if pygame.mouse.get_pressed()[0] == True:
            
        # error we need camera class probably due to scope

            offsetX = self.mouse_current_pos[0] - self.mouse_new_pos[0]
            offsetY = self.mouse_current_pos[1] - self.mouse_new_pos[1]

            self.camera[0] = self.camera[0] + offsetX
            self.camera[1] = self.camera[1] + offsetY
            # self.mouse_current_pos = (self.mouse_current_pos[0],self.mouse_current_pos[1])
            self.mouse_new_pos = self.mouse_current_pos
            
            print(f"Offset X: {offsetX}, Offset Y: {offsetY}")
            print(f"Camera: X: {self.camera[0]}, Camera Y: {self.camera[1]}")
    
import pygame
class Tree:

    def __init__(self,x,y, size,assets):
        # self.x = x
        # self.y = y
        self.location = (x,y)
        self.image_size = pygame.transform.scale(assets.tree_img, (size, size))
        self.wood = 6
        self.radius = 50
        # self.texture = 
        # self.width = width
        # self.height = height


    


import pygame
import random
class Tree:

    def __init__(self,x,y, size,assets):
        # self.x = x
        # self.y = y
        self.location = (x,y)
        self.image = pygame.transform.scale(assets.tree_img, (size, size))
        self.wood = random.randint(3,12)
        self.radius = 50
        # self.texture = 
        # self.width = width
        # self.height = height


    


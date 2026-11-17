import pygame
class BerryBush:
    def __init__(self, x, y, size, assets):
        self.location = (x,y)
        self.image_size = pygame.transform.scale(assets.berry_bush_image, (size, size))
        self.radius = 50



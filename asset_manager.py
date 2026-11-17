import pygame
class Asset_Manager:
    def __init__(self):
        pass

    def load_assets(self):

        self.tree_img = pygame.image.load("/Users/sammy/Programming/Python/Simulation/textures/tree.png").convert_alpha()
        self.berry_bush_ripe = pygame.image.load("/Users/sammy/Programming/Python/Simulation/textures/berry_bush.png").convert_alpha()
        self.berry_bush_unripe = pygame.image.load("/Users/sammy/Programming/Python/Simulation/textures/empty_berry_bush.png").convert_alpha()
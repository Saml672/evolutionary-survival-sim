import pygame
class Asset_Manager:
    def __init__(self):
        pass

    def load_assets(self):

        self.tree_img = pygame.image.load("/Users/sammy/Programming/Python/Simulation/my_game/assets/objects/tree/tree.png").convert_alpha()
        self.berry_bush_ripe = pygame.image.load("/Users/sammy/Programming/Python/Simulation/my_game/assets/objects/berry_bush/berry_bush.png").convert_alpha()
        self.berry_bush_unripe = pygame.image.load("/Users/sammy/Programming/Python/Simulation/my_game/assets/objects/berry_bush/empty_berry_bush.png").convert_alpha()
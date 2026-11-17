import pygame
class BerryBush:
    def __init__(self, x, y, size, assets):
        self.location = (x,y)
        self.ripe = assets.berry_bush_ripe
        self.unripe = assets.berry_bush_unripe
        self.fruit_ready = True
        self.image = pygame.transform.scale(self.fruit_state, (size, size))
        self.radius = 50


    @property
    def fruit_state(self):
        if (self.fruit_ready):
            self.image = self.ripe
            return self.image
        else:
            self.image = self.unripe
            return self.image

    



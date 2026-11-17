import pygame
from asset_manager import Asset_Manager
from objects.tree import Tree
from world_gen import World_Gen
import random
from renderer import draw
#pygame setup

pygame.init()
WORLD_WIDTH = 5000
WORLD_HEIGHT = 5000
width = 1280
height = 720
# mouse_object = pygame.mouse.get_pos()

half_width = width / 2
half_height = height / 2
screen = pygame.display.set_mode((width,height)) # actual screen size
clock = pygame.time.Clock()
running = True
asset_manage = Asset_Manager()

world_generation = World_Gen(asset_manage)

asset_manage.load_assets()
world_generation.generate_flora(half_width,half_height, asset_manage)


# Tree(350,350,50,asset_manage)
# name window
pygame.display.set_caption('Simulation')
# resize images
#img_large = pygame.transform.scale(img, (200, 200))
while running:

    #poll for events
    #pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to erase last frame
    screen.fill("cyan")

    # RENDER GAME HERE

    # the -150 is a offset to center landmass.
    pygame.draw.rect(screen, "green", (half_width - 300 ,half_height - 300,600,600))
    # attempting to draw trees
    for flora in world_generation.flora:
        draw(flora, screen,asset_manage)
    # screen.blit(asset_manage.img_small,(350,350))

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
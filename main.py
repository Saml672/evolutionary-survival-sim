import pygame
from asset_manager import Asset_Manager
from objects.tree import Tree
from world_gen import World_Gen
import renderer
from world import World
import controls
#pygame setup

pygame.init()


# mouse_object = pygame.mouse.get_pos()

world_object = World()
screen = pygame.display.set_mode((world_object.width,world_object.height)) # actual screen size
clock = pygame.time.Clock()
running = True
asset_manage = Asset_Manager()

world_generation = World_Gen(asset_manage)


asset_manage.load_assets()
world_generation.generate_flora(world_object.half_width,world_object.half_height, asset_manage)


# Tree(350,350,50,asset_manage)
# name window
pygame.display.set_caption('Simulation')
# resize images
#img_large = pygame.transform.scale(img, (200, 200))
while running:

    #poll for events
    #pygame.QUIT event means the user clicked X to close your window
    # for event in pygame.event.get():
    #     if event.type == pygame.QUIT:
    #         running = False

    running = controls.game_controls(world_object)
    # fill the screen with a color to erase last frame
    screen.fill("cyan")

    # RENDER GAME HERE

    # the -150 is a offset to center landmass.
    renderer.draw_landmass(pygame, screen, world_object)
    # pygame.draw.rect(screen, "green", ((world_object.half_width - 300) ,(world_object.half_height - 300),600,600))
    # attempting to draw trees
    for flora in world_generation.flora:
        renderer.draw_objects(flora, screen,world_object)
    # screen.blit(asset_manage.img_small,(350,350))

    # flip() the display to put your work on screen
    # world.mouse_position()
    world_object.move_camera()
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
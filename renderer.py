
from objects.berry_bush import BerryBush
world_offset = [0,0]
def draw_landmass(pygame,screen,world):
        world_offset[0] = (world.half_width - 300) - world.camera[0]
        world_offset[1] = (world.half_height - 300) - world.camera[1]
        pygame.draw.rect(screen, "green", (world_offset[0] ,world_offset[1],600,600))

def draw_objects(obj, screen,world):
    # have to fix trees not drawing here
    
    world_offset[0] = obj.location[0] - world.camera[0]
    world_offset[1] = obj.location[1] - world.camera[1]
    screen.blit(obj.image,world_offset)

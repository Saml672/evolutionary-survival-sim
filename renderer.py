
from objects.berry_bush import BerryBush

def draw(obj, screen,assets):
    # have to fix trees not drawing here
    screen.blit(obj.image,obj.location)

import random
import math
from objects.tree import Tree
from objects.berry_bush import BerryBush
# asset_manage = Asset_Manager()
class World_Gen:
    def __init__(self, assets):
        self.assets = assets
        self.trees = []
        self.berry_bushs = []
        self.flora = []




    def generate_flora(self, flora_x,flora_y,assets):
        """
        We need to add a random pool next. so bushes, rocks, etc can generate
        with the trees!
        """

        grid = [[None for j in range (10)] for i in range(10)]
        
        
        # print(vars(grid[0][0]))
        random_flora = random.randint(1,2)
        if (random_flora == 1):
            tree_shrub = Tree(flora_x,flora_y, 50, assets)
            grid[0][0] = tree_shrub
            self.trees.append(tree_shrub)
            self.flora.append(tree_shrub)
            
        elif (random_flora == 2):
            berry_bush_shrub = BerryBush(flora_x, flora_y, 20, assets)
            grid[0][0] = berry_bush_shrub
            self.berry_bushs.append(berry_bush_shrub)
            self.flora.append(berry_bush_shrub)


        
        
        
        for i in range(10):
            for j in range(10):
                    
                object_x = flora_x + random.randint(-250,250)
                object_y = flora_y + random.randint(-250,250)
                counter = 0
                for k in range(len(self.flora)):
                    
                    distance = math.sqrt((object_x - self.flora[k].location[0])**2 + (object_y - self.flora[k].location[1])**2)
                    if (distance > self.flora[k].radius):
                        counter += 1
                        if (counter == len(self.flora)):
                            random_flora = random.randint(1 , 2)
                            if (random_flora == 1):
                                tree_shrub = Tree(object_x,object_y, 50, assets)
                                grid[i][j] = tree_shrub
                                self.trees.append(tree_shrub)
                                self.flora.append(tree_shrub)
                                
                            elif (random_flora == 2):
                                berry_bush_shrub = BerryBush(object_x, object_y, 20, assets)
                                grid[0][0] = berry_bush_shrub
                                self.berry_bushs.append(berry_bush_shrub)
                                self.flora.append(berry_bush_shrub)
                    
                            
                    # if (distance > tree_list[k][3]):





                

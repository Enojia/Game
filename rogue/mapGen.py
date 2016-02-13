import libtcodpy as libtcod

##map and dongeon generator
class Dongeon:
    
    def __init__(self, map_width, map_height):
        self.map_width = map_width
        self.map_height = map_height
        self.map = [[Tile(False)
                     for y in range(map_height)]
                        for x in range(map_width)]
    
    
    
    color_dark_wall = libtcod.Color(0,0,100)
    color_dark_ground = libtcod.Color(50,50,150)
    
    class Tile:
        def __init__(self, blocked, block_sight = None):
            self.blocked = blocked
            if block_sight is None:
                block_sight = blocked
            self.block_sight = block_sight
            
    
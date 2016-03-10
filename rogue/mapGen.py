import libtcodpy as libtcod

##map and dongeon generator
class Dongeon:
    
    def __init__(self, map_width, map_height):
        self.map_width = map_width
        self.map_height = map_height
        self.map = [[Tile(True)
                     for y in range(map_height)]
                        for x in range(map_width)]
        rooms = []
        self.num_rooms = 0
        for r in range(30):
            w = libtcod.random_get_int(0, 6, 10)
            h = libtcod.random_get_int(0, 6, 10)
            x = libtcod.random_get_int(0,0,80 - w - 1)
            y = libtcod.random_get_int(0,0,45 - h - 1)
            new_room = Rect(x, y, w, h)
            failed = False
            for other_room in rooms:
                if new_room.intersect(other_room):
                    failed = True
                    break
            if not failed:
                self.create_room(new_room)
                (new_x, new_y) = new_room.center()
                if self.num_rooms == 0:
                    self.startX = new_x
                    self.startY = new_y
                else:
                    (prev_x, prev_y) = rooms[self.num_rooms-1].center()
                    
                    if libtcod.random_get_int(0,0,1) == 1:
                        self.create_h_tunnel(prev_x, new_x, prev_y)
                        self.create_v_tunnel(prev_y, new_y, new_x)
                    else:
                        self.create_v_tunnel(prev_y, new_y, prev_x)
                        self.create_h_tunnel(prev_x, new_x, new_y)
                rooms.append(new_room)
                self.num_rooms += 1
        print "num_rooms %d" %(self.num_rooms)
        print rooms
            
        
    color_dark_wall = libtcod.Color(0,0,100)
    color_dark_ground = libtcod.Color(50,50,150)
    
    def create_room(self,room):
        for x in range(room.x1 + 1, room.x2):
            for y in range(room.y1 + 1, room.y2):
                self.map[x][y].blocked = False
                self.map[x][y].block_sight = False
    def create_h_tunnel(self, x1, x2, y):
        for x in range(min(x1, x2), max(x1, x2)+1):
            self.map[x][y].blocked = False
            self.map[x][y].block_sight = False
    def create_v_tunnel(self, y1, y2, x):
        for y in range(min(y1, y2), max(y1, y2)+1):
            self.map[x][y].blocked = False
            self.map[x][y].block_sight = False
    
class Tile:
    def __init__(self, blocked, block_sight = None):
        self.blocked = blocked
        if block_sight is None:
            block_sight = blocked
            self.block_sight = block_sight
            
class Rect:
    def __init__(self, x, y, w, h):
        self.x1 = x
        self.y1 = y
        self.x2 = x + w
        self.y2 = y + h
    def center(self):
        center_x = (self.x1 + self.x2)/2
        center_y = (self.y1 + self.y2)/2
        return (center_x,center_y)
    def intersect(self, other):
        return (self.x1 <= other.x2 and self.x2 >= other.x1 and self.y1 <= other.y2 and self.y2 >= other.y1)
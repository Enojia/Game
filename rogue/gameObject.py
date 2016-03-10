import libtcodpy as libtcod

class Object(object):
    def __init__(self, x, y, char, color, dongeon):
        self.x = x
        self.y = y
        self.char = char
        self.color = color
        self.dongeon = dongeon

    def move(self, dx, dy):
        if not self.dongeon.map[self.x + dx][self.y + dy].blocked:
            self.x += dx
            self.y += dy
    
    def draw(self, con):
        libtcod.console_set_default_foreground(con, self.color)
        libtcod.console_put_char(con, self.x, self.y,self.char ,libtcod.BKGND_NONE)
    def clear(self,con):
        libtcod.console_put_char(con, self.x, self.y,' ',libtcod.BKGND_NONE)

class Player(Object):
    def handle_keys(self):
        global playerx, playery ##static variables        
        ## character controler 
        if libtcod.console_is_key_pressed(libtcod.KEY_UP):
            self.move(0,-1)
        elif libtcod.console_is_key_pressed(libtcod.KEY_DOWN):
            self.move(0,1)
        elif libtcod.console_is_key_pressed(libtcod.KEY_LEFT):
            self.move(-1,0)
        elif libtcod.console_is_key_pressed(libtcod.KEY_RIGHT):
            self.move(1,0)
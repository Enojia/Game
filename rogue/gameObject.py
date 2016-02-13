import libtcodpy as libtcod

class Object:
    def __init__(self, x, y, char, color):
        self.x = x
        self.y = y
        self.char = char
        self.color =color

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
    
    def draw(self):
        libtcod.console_set_default_foreground(con, self.color)
        libtcod.console_put_char(con, self.x, self.y,self.char ,libtcod.BKGND_NONE)
    def clear(self):
        libtcod.console_put_char(con, self.x, self.y,' ',libtcod.BKGND_NONE)

class Player(Object):
    def handle_keys():
        global playerx, playery ##static variables

        key = libtcod.console_wait_for_keypress(True)

        if key.vk == libtcod.KEY_ENTER and key.lalt:
            libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())
        elif key.vk == libtcod.KEY_ESCAPE:
            return True ## exit function
    
        ## character controler 
        if libtcod.console_is_key_pressed(libtcod.KEY_UP):
            player.move(0,1)
        elif libtcod.console_is_key_pressed(libtcod.KEY_DOWN):
            player.move(0,-1)
        elif libtcod.console_is_key_pressed(libtcod.KEY_LEFT):
            player.move(-1,0)
        elif libtcod.console_is_key_pressed(libtcod.KEY_RIGHT):
            player.move(1,0)
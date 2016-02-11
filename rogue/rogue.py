import libtcodpy as libtcod

SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50
LIMIT_FPS = 20

##we define a class to handle player, item etc
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
        libtcod.console_set_default_foreground(0, self.color)
        libtcod.console_put_char(0, self.x, self.y,self.char ,libtcod.BKGND_NONE)
    def clear(self):
        libtcod.console_put_char(0, self.x, self.y,' ',libtcod.BKGND_NONE)

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


##Initialization
libtcod.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, '~/Documents/rogue ', False)
libtcod.sys_set_fps(LIMIT_FPS)
con = libtcod.console_new(SCREEN_WIDTH, SCREEN_HEIGHT)

player = Object(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, "@", libtcod.white)
npc = Object(SCREEN_WIDTH/2 - 5, SCREEN_HEIGHT/2, "@", libtcod.yellow)
objects = [player, npc]
##main loop

while not libtcod.console_is_window_closed():
    for obj in objects:
        obj.draw()

    libtcod.console_blit(con, 0, 0, SCREEN_WIDTH, SCREEN_HEIGHT,0, 0, 0)
    libtcod.console_flush() ##redraw the scene
    
    for obj in objects:
        obj.clear()

    exit = handle_keys()
    if exit:
        break


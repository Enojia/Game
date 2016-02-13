import libtcodpy as libtcod
import gameObject

SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50
LIMIT_FPS = 20


##Initialization
libtcod.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, '~/Documents/rogue ', False)
libtcod.sys_set_fps(LIMIT_FPS)
con = libtcod.console_new(SCREEN_WIDTH, SCREEN_HEIGHT)

player = gameObject.Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, "@", libtcod.white)
npc = gameObject.Object(SCREEN_WIDTH/2 - 5, SCREEN_HEIGHT/2, "@", libtcod.yellow) ##change this later
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


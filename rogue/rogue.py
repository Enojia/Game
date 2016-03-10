import libtcodpy as libtcod
import gameObject
import mapGen
import render

SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50
LIMIT_FPS = 20


##Initialization
libtcod.console_set_custom_font('dejavu16x16_gs_tc.png', libtcod.FONT_TYPE_GRAYSCALE | libtcod.FONT_LAYOUT_TCOD)
libtcod.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, '~//Documents//rogue ', False)
libtcod.sys_set_fps(LIMIT_FPS)
con = libtcod.console_new(SCREEN_WIDTH, SCREEN_HEIGHT)

dongeon = mapGen.Dongeon(80, 45)
player = gameObject.Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, "@", libtcod.white, dongeon)
player.x = 25
player.y = 23
npc = gameObject.Object(SCREEN_WIDTH/2 - 5, SCREEN_HEIGHT/2, "@", libtcod.yellow, dongeon) ##change this later
objects = [player, npc]
##main loop


while not libtcod.console_is_window_closed():
    
    render.render_all(objects, dongeon, con)

    libtcod.console_blit(con, 0, 0, SCREEN_WIDTH, SCREEN_HEIGHT,0, 0, 0)
    libtcod.console_flush() ##redraw the scene
    
    for obj in objects:
        obj.clear(con)
        
    def handle_keys():
        key = libtcod.console_wait_for_keypress(False)
        if key.vk == libtcod.KEY_ENTER and key.lalt:
            libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())
        elif key.vk == libtcod.KEY_ESCAPE:
            return True ## exit function
    exit = handle_keys()
    if exit:
        break
    player.handle_keys()


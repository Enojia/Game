import libtcodpy as libtcod

def render_all(objects, map):
    for obj in objects:
        obj.draw()
    
    for y in range(map.MAP_HEIGHT):
        for x in range(map.MAP_WIDTH):
            wall = map.map[x][y].block_sight
            if wall:
                libtcod.console_set_char_background(con, x, y, map.color_dark_wall, libtcod.BKGND_SET)
            else:
                libtcod.console_set_char_background(con, x, y, map.color_dark_ground, libtcod.BKGND_SET)
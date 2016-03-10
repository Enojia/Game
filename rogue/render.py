import libtcodpy as libtcod

def render_all(objects, dongeon, con):
    for obj in objects:
        obj.draw(con)
    
    for y in range(dongeon.map_height):
        for x in range(dongeon.map_width):
            wall = dongeon.map[x][y].block_sight
            if wall:
                libtcod.console_set_char_background(con, x, y, dongeon.color_dark_wall, libtcod.BKGND_SET)
            else:
                libtcod.console_set_char_background(con, x, y, dongeon.color_dark_ground, libtcod.BKGND_SET)
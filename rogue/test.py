import libtcodpy as libtcod

off1 = libtcod.console_new(80, 50)
libtcod.console_blit(off1, 0, 0, 80, 50, 0, 0, 0)
libtcod.console_flush()
libtcod.console_wait_for_keypress(True)

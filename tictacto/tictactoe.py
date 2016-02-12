#!/bin/usr/Python2

##initializing board
    
def display():
    for arr in game:
        print arr

def rule(array):
    if array[0][0]==1 and array[0][1]==1 and array[0][2] == 1:
        print "Player one win"
        return True
    if array[0][0]==2 and array[0][1]==2 and array[0][2] == 2:
        print "Player two win"
        return True
    if array[1][0]==1 and array[1][1]==1 and array[1][2] == 1:
        print "Player one win"
        return True
    if array[1][0]==2 and array[1][1]==2 and array[1][2] == 2:
        print "Player two win"
        return True
    if array[2][0]==1 and array[2][1]==1 and array[2][2] == 1:
        print "Player one win"
        return True
    if array[2][0]==2 and array[2][1]==2 and array[2][2] == 2:
        print "Player two win"
        return True
##vertical check
    if array[0][0]==1 and array[1][0]==1 and array[2][0] == 1:
        print "Player one win"
        return True
    if array[0][0]==2 and array[1][0]==2 and array[2][0] == 2:
        print "Player two win"
        return True
    if array[0][1]==1 and array[1][1]==1 and array[2][1] == 1:
        print "Player one win"
        return True
    if array[0][1]==2 and array[1][1]==2 and array[2][1] == 2:
        print "Player two win"
        return True
    if array[0][2]==1 and array[1][2]==1 and array[2][2] == 1:
        print "Player one win"
        return True
    if array[0][2]==2 and array[1][2]==2 and array[2][2] == 2:
        print "Player two win"
        return True





game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]

player1_turn = True
player = 1
array = []

while True:
    if player1_turn == True:
        player = 1
    else:
        player = 2
    print player
    coord = raw_input("Enter where you want to play \"x,y\"   ")
    coord.strip()
    array = coord.split(",")
    addr1 = int(array[0])
    addr2 = int(array[1])
    while(addr1 > 2 or addr1 < 0 or addr2 > 2 or addr2 < 0 or game[addr2][addr1] != 0):
        coord = raw_input("Enter again wrong number  ")
        coord.strip()
        array = coord.split(",")
        addr1 = int(array[0])
        addr2 = int(array[1])

    game[addr2][addr1] = player
    if player1_turn:
        player1_turn = False
    else:
        player1_turn = True
    print player1_turn
    display()
    stop = rule(game)
    if stop == True:
        break

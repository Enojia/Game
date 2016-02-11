#!/bin/usr/Python2

##initializing board
    
def display():
    print game

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
    while(game[addr1][addr2] != 0):
        coord = raw_input("Enter again wrong number")
    game[addr1][addr2] = player
    if player1_turn:
        player1_turn = False
    else:
        player1_turn = True
    print player1_turn

    display()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#%%
#boards

board = [
['x', 'o', 'x'],
['o', 'x', 'o'],
['o', 'x', 'x']
]

board2 = [
['x', 'x', 'x'],
['o', 'x', 'o'],
['x', 'o', 'x']
]


board3 = [
['x', 'x', 'x'],
['x', 'x', 'o'],
['x', 'o', 'x']
]


board4 = [
['x', 'x', 'x','o'],
['x', 'x', 'o','x'],
['x', 'x', 'x','o'],
['o', 'x', 'x','o']
]

board5 = [
['x', 'x', 'x','x'],
['x', 'o', 'x','x'],
['x', 'x', 'x','o'],
['x', 'x', 'x','o']
]

#%%
#Create a function solved_horizontal that check if player
#using as their stone won a game (by putting three 'x' in a row) given
#a final board. The board is a two dimensional list:

def solved_horizontal(lst):
    solved = False
    for x in range(len(lst)):
        counter = 0
        for y in range(len(lst)):
            if lst[x][y] == 'x':
                counter += 1
            if counter == len(lst):
                solved = True
    return solved   

#function works also for lists bigger than 3     
                
#%%Create a function solved_vertical that checks if player
#using 'x' as their stone won a game (by putting three 'x' in a column)
#given a final board.

def solved_vertical(lst):
    solved = False
    for y in range(len(lst)):
        counter = 0
        for x in range(len(lst)):
            if lst[x][y] == 'x':
                counter += 1
            if counter == len(lst):
                solved = True
    return solved  

#function works also for lists bigger than 3

#%%Create a function solved_diagonal that checks if player
#using 'x' as their stone won a game (by putting three 'x' in a diagonal)
#given a final board

def solved_diagonal(lst):
    solved = False
    x = 0
    y = 0
    a = 0
    b = len(lst) - 1
    while x < len(lst) and a < len(lst):
        if lst[x][y] == 'x':
            x += 1
            y += 1    
        elif lst[a][b] == 'x':
            a += 1
            b -= 1   
        else:
            return solved      
    solved = True    
    return solved  
      
#function works also for lists bigger than 3

#%%Create a function solved_tictactoe that checks if
#player using 'x' as their stone won a game

def solved_tictactoe(lst):
    return solved_horizontal(lst) or solved_vertical(lst) or solved_diagonal(lst)

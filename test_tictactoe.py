# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 09:21:47 2018

@author: tancr
"""
#%%
from tictactoe import solved_tictactoe

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
['x', 'o', 'x','o'],
['o', 'x', 'x','o']
]

board5 = [
['x', 'x', 'x','x'],
['x', 'o', 'x','x'],
['x', 'x', 'x','o'],
['x', 'x', 'x','o']
]


def test_tictactoe():
    assert solved_tictactoe(board) == True
    assert solved_tictactoe(board2) == True
    assert solved_tictactoe(board3) == True
    assert solved_tictactoe(board4) == False
    assert solved_tictactoe(board5) == True
    
    
    
    
    
    
    

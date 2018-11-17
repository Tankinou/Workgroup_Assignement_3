# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 18:48:22 2018

@author: Grani
"""
#%%
rock = "rock"
paper = "paper"
scissors = "scissors"
lizard = "lizard"
spock = "spock"


def rock_paper_scissors_lizard_spock(player1, player2):
    if player1 == player2:
        return "Draw"
    elif player1 == "rock" and player2 == "paper":
        return "Player 2 won"
    elif player1 == "paper" and player2 == "rock":
        return "Player 1 won"
    elif player1 == "rock" and player2 == "scissors":
        return "Player 1 won"
    elif player1 == "scissors" and player2 == "rock":
        return "Player 2 won"
    elif player1 == "scissors" and player2 == "paper":
        return "Player 1 won"
    elif player1 == "paper" and player2 == "scissors":
        return "Player 2 won"
    elif player1 == "spock" and player2 == "lizard":
        return "Player 2 won"
    elif player1 == "lizard" and player2 == "spock":
        return "Player 1 won"
    elif player1 == "spock" and player2 == "scissors":
        return "Player 1 won"
    elif player1 == "scissors" and player2 == "spock":
        return "Player 2 won"
    elif player1 == "spock" and player2 == "paper":
        return "Player 2 won"
    elif player1 == "paper" and player2 == "spock":
        return "Player 1 won"
    elif player1 == "spock" and player2 == "rock":
        return "Player 1 won"
    elif player1 == "rock" and player2 == "spock":
        return "Player 2 won"
    elif player1 == "lizard" and player2 == "scissors":
        return "Player 2 won"
    elif player1 == "scissors" and player2 == "lizard":
        return "Player 1 won"
    elif player1 == "lizard" and player2 == "paper":
        return "Player 1 won"
    elif player1 == "paper" and player2 == "lizard":
        return "Player 2 won"
    elif player1 == "lizard" and player2 == "rock":
        return "Player 2 won"
    elif player1 == "rock" and player2 == "lizard":
        return "Player 1 won"
    else:
        return None
#%%
        
#Alternative solution :)    
        
    
def rock_paper_scissors_spock_inCool(player1,player2):
    key = {"rock":0,"spock":1,"paper":2,"lizard":3,"scissors":4}
    n1 = key[player1]
    n2 = key[player2]
    dif = (n1 - n2)%5
    if dif == 0:
        return "Draw"
    elif dif == 1 or dif == 2:
        return "Player 1 won"
    elif dif == 3 or dif == 4:
        return "Player 2 won"
    else:
        return None
#%%    
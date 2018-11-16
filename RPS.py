# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 08:48:10 2018

@author: Grani
"""

rock = "rock"
paper = "paper"
scissors = "scissors"


def rock_paper_scissors(player1, player2):
    "this function hardcodes the respective results"
    if player1 == "rock" and player2 == "paper":
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
    elif player1 == player2:
        return "Draw"
    else:
        return None
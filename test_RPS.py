# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 09:36:27 2018

@author: Grani
"""

from RPS import rock_paper_scissors

rock = "rock"
paper = "paper"
scissors = "scissors"

def test_rock_paper_scissors():
    assert rock_paper_scissors(rock, rock) == "Draw"
    assert rock_paper_scissors(rock, paper) == "Player 2 won"
    assert rock_paper_scissors(rock, scissors) == "Player 1 won"
    assert rock_paper_scissors(paper, paper) == "Draw"
    assert rock_paper_scissors(paper, rock) == "Player 1 won"
    assert rock_paper_scissors(paper, scissors) == "Player 2 won"
    assert rock_paper_scissors(scissors, scissors) == "Draw"
    assert rock_paper_scissors(scissors, rock) == "Player 2 won"
    assert rock_paper_scissors(scissors, paper) == "Player 1 won"
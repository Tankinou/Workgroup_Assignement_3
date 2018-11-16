# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 19:11:14 2018

@author: Grani
"""

from RPSLS import rock_paper_scissors_lizard_spock

rock = "rock"
paper = "paper"
scissors = "scissors"
lizard = "lizard"
spock = "spock"

def test_rock_paper_scissors_lizard_spock():
    assert rock_paper_scissors_lizard_spock(rock, rock) == "Draw"
    assert rock_paper_scissors_lizard_spock(rock, paper) == "Player 2 won"
    assert rock_paper_scissors_lizard_spock(rock, scissors) == "Player 1 won"
    assert rock_paper_scissors_lizard_spock(paper, paper) == "Draw"
    assert rock_paper_scissors_lizard_spock(paper, rock) == "Player 1 won"
    assert rock_paper_scissors_lizard_spock(paper, scissors) == "Player 2 won"
    assert rock_paper_scissors_lizard_spock(scissors, scissors) == "Draw"
    assert rock_paper_scissors_lizard_spock(scissors, rock) == "Player 2 won"
    assert rock_paper_scissors_lizard_spock(scissors, paper) == "Player 1 won"
    assert rock_paper_scissors_lizard_spock(lizard, lizard) == "Draw"
    assert rock_paper_scissors_lizard_spock(spock, spock) == "Draw"
    assert rock_paper_scissors_lizard_spock(lizard, spock) == "Player 1 won"
    assert rock_paper_scissors_lizard_spock(spock, lizard) == "Player 2 won"
    assert rock_paper_scissors_lizard_spock(lizard, rock) == "Player 2 won"
    assert rock_paper_scissors_lizard_spock(rock, lizard) == "Player 1 won"
    assert rock_paper_scissors_lizard_spock(lizard, paper) == "Player 1 won"
    assert rock_paper_scissors_lizard_spock(paper, lizard) == "Player 2 won"
    assert rock_paper_scissors_lizard_spock(lizard, scissors) == "Player 2 won"
    assert rock_paper_scissors_lizard_spock(scissors, lizard) == "Player 1 won"
    assert rock_paper_scissors_lizard_spock(spock, rock) == "Player 1 won"
    assert rock_paper_scissors_lizard_spock(rock, spock) == "Player 2 won"
    assert rock_paper_scissors_lizard_spock(spock, scissors) == "Player 1 won"
    assert rock_paper_scissors_lizard_spock(scissors, spock) == "Player 2 won"
    assert rock_paper_scissors_lizard_spock(spock, paper) == "Player 2 won"
    assert rock_paper_scissors_lizard_spock(paper, spock) == "Player 1 won"
    
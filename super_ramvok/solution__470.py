
# -*- coding: utf-8 -*-
'''
    File name: super_ramvok\solution__470.py
    Author: Vaidic Joshi
    Date created: Oct 18, 2018
    Python Version: 3.x
'''

# Solution to Project Euler Problem #470 :: Super Ramvok
# 
# For more information see:
# https://projecteuler.net/problem=470

# Problem Statement 
'''
b'Consider a single game of Ramvok:\n\nLet t represent the maximum number of turns the game lasts. If t = 0, then the game ends immediately. Otherwise, on each turn i, the player rolls a die. After rolling, if i < t the player can either stop the game and receive a prize equal to the value of the current roll, or discard the roll and try again next turn. If i = t, then the roll cannot be discarded and the prize must be accepted. Before the game begins, t is chosen by the player, who must then pay an up-front cost ct for some constant c. For c = 0, t can be chosen to be infinite (with an up-front cost of 0). Let R(d, c) be the expected profit (i.e. net gain) that the player receives from a single game of optimally-played Ramvok, given a fair d-sided die and cost constant c. For example, R(4, 0.2) = 2.65. Assume that the player has sufficient funds for paying any/all up-front costs.\n\nNow consider a game of Super Ramvok:\n\nIn Super Ramvok, the game of Ramvok is played repeatedly, but with a slight modification. After each game, the die is altered. The alteration process is as follows: The die is rolled once, and if the resulting face has its pips visible, then that face is altered to be blank instead. If the face is already blank, then it is changed back to its original value. After the alteration is made, another game of Ramvok can begin (and during such a game, at each turn, the die is rolled until a face with a value on it appears). The player knows which faces are blank and which are not at all times. The game of Super Ramvok ends once all faces of the die are blank.\n\nLet S(d, c) be the expected profit that the player receives from an optimally-played game of Super Ramvok, given a fair d-sided die to start (with all sides visible), and cost constant c. For example, S(6, 1) = 208.3.\n\nLet F(n) = \xe2\x88\x914\xe2\x89\xa4d\xe2\x89\xa4n \xe2\x88\x910\xe2\x89\xa4c\xe2\x89\xa4n S(d, c).\n\nCalculate F(20), rounded to the nearest integer.'
'''

# Solution 

# Solution Approach 
'''
'''

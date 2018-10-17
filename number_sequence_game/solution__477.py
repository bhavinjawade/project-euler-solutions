
# -*- coding: utf-8 -*-
'''
    File name: number_sequence_game\solution__477.py
    Author: Vaidic Joshi
    Date created: Oct 18, 2018
    Python Version: 3.x
'''

# Solution to Project Euler Problem #477 :: Number Sequence Game
# 
# For more information see:
# https://projecteuler.net/problem=477

# Problem Statement 
'''
b'The number sequence game starts with a sequence S of N numbers written on a line.\nTwo players alternate turns. At his turn, a player must select and remove either the first or the last number remaining in the sequence.\nThe player score is the sum of all the numbers he has taken. Each player attempts to maximize his own sum.\nIf N = 4 and S = {1, 2, 10, 3}, then each player maximizes his score as follows:\nPlayer 1: removes the first number (1)\nPlayer 2: removes the last number from the remaining sequence (3)\nPlayer 1: removes the last number from the remaining sequence (10)\nPlayer 2: removes the remaining number (2)\nPlayer 1 score is 1 + 10 = 11.\nLet F(N) be the score of player 1 if both players follow the optimal strategy for the sequence S = {s1, s2,\xc2\xa0...,\xc2\xa0sN} defined as:\ns1 = 0\nsi+1 = (si2 + 45) modulo 1 000 000 007\nThe sequence begins with S\xc2\xa0=\xc2\xa0{0,\xc2\xa045,\xc2\xa02070,\xc2\xa04284945,\xc2\xa0753524550,\xc2\xa0478107844,\xc2\xa0894218625,\xc2\xa0...}.\nYou are given F(2)\xc2\xa0=\xc2\xa045, F(4)\xc2\xa0=\xc2\xa04284990, F(100)\xc2\xa0=\xc2\xa026365463243, F(104)\xc2\xa0=\xc2\xa02495838522951.\nFind F(108).'
'''

# Solution 

# Solution Approach 
'''
'''

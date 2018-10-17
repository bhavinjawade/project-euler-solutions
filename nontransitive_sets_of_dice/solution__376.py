
# -*- coding: utf-8 -*-
'''
    File name: nontransitive_sets_of_dice\solution__376.py
    Author: Vaidic Joshi
    Date created: Oct 18, 2018
    Python Version: 3.x
'''

# Solution to Project Euler Problem #376 :: Nontransitive sets of dice
# 
# For more information see:
# https://projecteuler.net/problem=376

# Problem Statement 
'''
b'Consider the following set of dice with nonstandard pips:\n\n\n\nDie A: 1 4 4 4 4 4\nDie B: 2 2 2 5 5 5\nDie C: 3 3 3 3 3 6\n\n\nA game is played by two players picking a die in turn and rolling it. The player who rolls the highest value wins.\n\n\n\nIf the first player picks die A and the second player picks die B we get\nP(second player wins) = 7/12 > 1/2\n\n\nIf the first player picks die B and the second player picks die C we get\nP(second player wins) = 7/12 > 1/2\n\n\nIf the first player picks die C and the second player picks die A we get\nP(second player wins) = 25/36 > 1/2\n\n\nSo whatever die the first player picks, the second player can pick another die and have a larger than 50% chance of winning.\nA set of dice having this property is called a nontransitive set of dice.\n\n\n\nWe wish to investigate how many sets of nontransitive dice exist. We will assume the following conditions:There are three six-sided dice with each side having between 1 and N pips, inclusive.\nDice with the same set of pips are equal, regardless of which side on the die the pips are located.\nThe same pip value may appear on multiple dice; if both players roll the same value neither player wins.\nThe sets of dice {A,B,C}, {B,C,A} and {C,A,B} are the same set.\n\nFor N = 7 we find there are 9780 such sets.\nHow many are there for N = 30 ?'
'''

# Solution 

# Solution Approach 
'''
'''

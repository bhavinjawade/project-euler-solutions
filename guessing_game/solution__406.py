
# -*- coding: utf-8 -*-
'''
    File name: guessing_game\solution__406.py
    Author: Vaidic Joshi
    Date created: Oct 18, 2018
    Python Version: 3.x
'''

# Solution to Project Euler Problem #406 :: Guessing Game
# 
# For more information see:
# https://projecteuler.net/problem=406

# Problem Statement 
'''
b'We are trying to find a hidden number selected from the set of integers {1, 2, ..., n} by asking questions. \nEach number (question) we ask, we get one of three possible answers: "Your guess is lower than the hidden number" (and you incur a cost of a), or\n "Your guess is higher than the hidden number" (and you incur a cost of b), or\n "Yes, that\'s it!" (and the game ends).\nGiven the value of n, a, and b, an optimal strategy minimizes the total cost for the worst possible case.\n\nFor example, if n = 5, a = 2, and b = 3, then we may begin by asking "2" as our first question.\n\nIf we are told that 2 is higher than the hidden number (for a cost of b=3), then we are sure that "1" is the hidden number (for a total cost of 3).\nIf we are told that 2 is lower than the hidden number (for a cost of a=2), then our next question will be "4".\nIf we are told that 4 is higher than the hidden number (for a cost of b=3), then we are sure that "3" is the hidden number (for a total cost of 2+3=5).\nIf we are told that 4 is lower than the hidden number (for a cost of a=2), then we are sure that "5" is the hidden number (for a total cost of 2+2=4).\nThus, the worst-case cost achieved by this strategy is 5. It can also be shown that this is the lowest worst-case cost that can be achieved. \nSo, in fact, we have just described an optimal strategy for the given values of n, a, and b.\n\nLet C(n, a, b) be the worst-case cost achieved by an optimal strategy for the given values of n, a, and b.\n\nHere are a few examples:\nC(5, 2, 3) = 5\nC(500, \xe2\x88\x9a2, \xe2\x88\x9a3) = 13.22073197...\nC(20000, 5, 7) = 82\nC(2000000, \xe2\x88\x9a5, \xe2\x88\x9a7) = 49.63755955...\n\nLet Fk be the Fibonacci numbers: Fk = Fk-1 + Fk-2 with base cases F1 = F2 = 1.Find \xe2\x88\x911\xe2\x89\xa4k\xe2\x89\xa430\xc2\xa0C(1012, \xe2\x88\x9ak, \xe2\x88\x9aFk), and give your answer rounded to 8 decimal places behind the decimal point.'
'''

# Solution 

# Solution Approach 
'''
'''

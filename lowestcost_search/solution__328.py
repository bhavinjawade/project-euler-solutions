
# -*- coding: utf-8 -*-
'''
    File name: lowestcost_search\solution__328.py
    Author: Vaidic Joshi
    Date created: Oct 18, 2018
    Python Version: 3.x
'''

# Solution to Project Euler Problem #328 :: Lowest-cost Search
# 
# For more information see:
# https://projecteuler.net/problem=328

# Problem Statement 
'''
b'We are trying to find a hidden number selected from the set of integers {1, 2, ..., n} by asking questions. \nEach number (question) we ask, has a cost equal to the number asked and we get one of three possible answers: "Your guess is lower than the hidden number", or\n "Yes, that\'s it!", or\n "Your guess is higher than the hidden number".\nGiven the value of n, an optimal strategy minimizes the total cost (i.e. the sum of all the questions asked) for the worst possible case. E.g.\n\nIf n=3, the best we can do is obviously to ask the number "2". The answer will immediately lead us to find the hidden number (at a total cost = 2).\n\nIf n=8, we might decide to use a "binary search" type of strategy: Our first question would be "4" and if the hidden number is higher than 4 we will need one or two additional questions.\nLet our second question be "6". If the hidden number is still higher than 6, we will need a third question in order to discriminate between 7 and 8.\nThus, our third question will be "7" and the total cost for this worst-case scenario will be 4+6+7=17.\n\nWe can improve considerably the worst-case cost for n=8, by asking "5" as our first question.\nIf we are told that the hidden number is higher than 5, our second question will be "7", then we\'ll know for certain what the hidden number is (for a total cost of 5+7=12).\nIf we are told that the hidden number is lower than 5, our second question will be "3" and if the hidden number is lower than 3 our third question will be "1", giving a total cost of 5+3+1=9.\nSince 12>9, the worst-case cost for this strategy is 12. That\'s better than what we achieved previously with the "binary search" strategy; it is also better than or equal to any other strategy.\nSo, in fact, we have just described an optimal strategy for n=8.\n\nLet C(n) be the worst-case cost achieved by an optimal strategy for n, as described above.\nThus C(1) = 0, C(2) = 1, C(3) = 2 and C(8) = 12.\nSimilarly, C(100) = 400 and C(n) = 17575.\n\nFind C(n).'
'''

# Solution 

# Solution Approach 
'''
'''

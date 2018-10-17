
# -*- coding: utf-8 -*-
'''
    File name: randomized_binary_search\solution__527.py
    Author: Vaidic Joshi
    Date created: Oct 18, 2018
    Python Version: 3.x
'''

# Solution to Project Euler Problem #527 :: Randomized Binary Search
# 
# For more information see:
# https://projecteuler.net/problem=527

# Problem Statement 
'''
b'A secret integer t is selected at random within the range 1 \xe2\x89\xa4 t \xe2\x89\xa4 n. \n\nThe goal is to guess the value of t by making repeated guesses, via integer g. After a guess is made, there are three possible outcomes, in which it will be revealed that either g < t, g = t, or g > t. Then the process can repeat as necessary.\n\nNormally, the number of guesses required on average can be minimized with a binary search: Given a lower bound L and upper bound H (initialized to L = 1 and H = n), let g = \xe2\x8c\x8a(L+H)/2\xe2\x8c\x8b where \xe2\x8c\x8a\xe2\x8b\x85\xe2\x8c\x8b is the integer floor function. If g = t, the process ends. Otherwise, if g < t, set L = g+1, but if g > t instead, set H = g\xe2\x88\x921. After setting the new bounds, the search process repeats, and ultimately ends once t is found. Even if t can be deduced without searching, assume that a search will be required anyway to confirm the value.\n\nYour friend Bob believes that the standard binary search is not that much better than his randomized variant: Instead of setting g = \xe2\x8c\x8a(L+H)/2\xe2\x8c\x8b, simply let g be a random integer between L and H, inclusive. The rest of the algorithm is the same as the standard binary search. This new search routine will be referred to as a random binary search.\n\nGiven that 1 \xe2\x89\xa4 t \xe2\x89\xa4 n for random t, let B(n) be the expected number of guesses needed to find t using the standard binary search, and let R(n) be the expected number of guesses needed to find t using the random binary search. For example, B(6) = 2.33333333 and R(6) = 2.71666667 when rounded to 8 decimal places.\n\nFind R(1010) \xe2\x88\x92 B(1010) rounded to 8 decimal places.'
'''

# Solution 

# Solution Approach 
'''
'''

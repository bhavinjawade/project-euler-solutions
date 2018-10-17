
# -*- coding: utf-8 -*-
'''
    File name: infinite_string_tour\solution__238.py
    Author: Vaidic Joshi
    Date created: Oct 18, 2018
    Python Version: 3.x
'''

# Solution to Project Euler Problem #238 :: Infinite string tour
# 
# For more information see:
# https://projecteuler.net/problem=238

# Problem Statement 
'''
b'Create a sequence of numbers using the "Blum Blum Shub" pseudo-random number generator:\n\ns0\n    =\n    14025256\n  sn+1\n    =\n    sn2 mod 20300713\n  \n\nConcatenate these numbers \xe2\x80\x89s0s1s2\xe2\x80\xa6 to create a string w of infinite length.\nThen, w\xe2\x80\x89=\xe2\x80\x8914025256741014958470038053646\xe2\x80\xa6\n\nFor a positive integer k, if no substring of w exists with a sum of digits equal to k, p(k) is defined to be zero. If at least one substring of w exists with a sum of digits equal to k, we define p(k)\xe2\x80\x89=\xe2\x80\x89z, where z is the starting position of the earliest such substring.\n\nFor instance:\n\nThe substrings 1, 14, 1402, \xe2\x80\xa6 \nwith respective sums of digits equal to 1, 5, 7, \xe2\x80\xa6\nstart at position 1, hence p(1)\xe2\x80\x89=\xe2\x80\x89p(5)\xe2\x80\x89=\xe2\x80\x89p(7)\xe2\x80\x89=\xe2\x80\x89\xe2\x80\xa6\xe2\x80\x89=\xe2\x80\x891.\n\nThe substrings 4, 402, 4025, \xe2\x80\xa6\nwith respective sums of digits equal to 4, 6, 11, \xe2\x80\xa6\nstart at position 2, hence p(4)\xe2\x80\x89=\xe2\x80\x89p(6)\xe2\x80\x89=\xe2\x80\x89p(11)\xe2\x80\x89=\xe2\x80\x89\xe2\x80\xa6\xe2\x80\x89=\xe2\x80\x892.\n\nThe substrings 02, 0252, \xe2\x80\xa6\nwith respective sums of digits equal to 2, 9, \xe2\x80\xa6\nstart at position 3, hence p(2)\xe2\x80\x89=\xe2\x80\x89p(9)\xe2\x80\x89=\xe2\x80\x89\xe2\x80\xa6\xe2\x80\x89=\xe2\x80\x893.\n\nNote that substring 025 starting at position 3, has a sum of digits equal to 7, but there was an earlier substring (starting at position 1) with a sum of digits equal to 7, so p(7)\xe2\x80\x89=\xe2\x80\x891, not 3.\n\nWe can verify that, for 0\xe2\x80\x89<\xe2\x80\x89k\xe2\x80\x89\xe2\x89\xa4\xe2\x80\x89103, \xe2\x88\x91\xe2\x80\x89p(k) = 4742.\n\nFind \xe2\x88\x91\xe2\x80\x89p(k), for 0\xe2\x80\x89<\xe2\x80\x89k\xe2\x80\x89\xe2\x89\xa4\xe2\x80\x892\xc2\xb71015.'
'''

# Solution 

# Solution Approach 
'''
'''

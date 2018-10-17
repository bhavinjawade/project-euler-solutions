
# -*- coding: utf-8 -*-
'''
    File name: searching_for_a_maximumsum_subsequence\solution__149.py
    Author: Vaidic Joshi
    Date created: Oct 18, 2018
    Python Version: 3.x
'''

# Solution to Project Euler Problem #149 :: Searching for a maximum-sum subsequence
# 
# For more information see:
# https://projecteuler.net/problem=149

# Problem Statement 
'''
b'Looking at the table below, it is easy to verify that the maximum possible sum of adjacent numbers in any direction (horizontal, vertical, diagonal or anti-diagonal) is 16 (= 8 + 7 + 1).\n\n\n\xe2\x88\x9225329\xe2\x88\x926513273\xe2\x88\x9218\xe2\x88\x924\xc2\xa0 8\n\nNow, let us repeat the search, but on a much larger scale:\n\nFirst, generate four million pseudo-random numbers using a specific form of what is known as a "Lagged Fibonacci Generator":\n\nFor 1 \xe2\x89\xa4 k \xe2\x89\xa4 55, sk = [100003 \xe2\x88\x92 200003k + 300007k3] (modulo 1000000) \xe2\x88\x92 500000.\nFor 56 \xe2\x89\xa4 k \xe2\x89\xa4 4000000, sk = [sk\xe2\x88\x9224 + sk\xe2\x88\x9255 + 1000000] (modulo 1000000) \xe2\x88\x92 500000.\n\nThus, s10 = \xe2\x88\x92393027 and s100 = 86613.\n\nThe terms of s are then arranged in a 2000\xc3\x972000 table, using the first 2000 numbers to fill the first row (sequentially), the next 2000 numbers to fill the second row, and so on.\n\nFinally, find the greatest sum of (any number of) adjacent entries in any direction (horizontal, vertical, diagonal or anti-diagonal).'
'''

# Solution 

# Solution Approach 
'''
'''

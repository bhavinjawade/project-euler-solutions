
# -*- coding: utf-8 -*-
'''
    File name: collatz_prefix_families\solution__494.py
    Author: Vaidic Joshi
    Date created: Oct 18, 2018
    Python Version: 3.x
'''

# Solution to Project Euler Problem #494 :: Collatz prefix families
# 
# For more information see:
# https://projecteuler.net/problem=494

# Problem Statement 
'''
b'The Collatz sequence is defined as:\n$a_{i+1} = \\left\\{  \\large{\\frac {a_i} 2 \\atop 3 a_i+1} {\\text{if }a_i\\text{ is even} \\atop \\text{if }a_i\\text{ is odd}} \\right.$.\n\n\nThe Collatz conjecture states that starting from any positive integer, the sequence eventually reaches the cycle 1,4,2,1....\nWe shall define the sequence prefix p(n) for the Collatz sequence starting with a1 = n as the sub-sequence of all numbers not a power of 2 (20=1 is considered a power of 2 for this problem). For example:p(13) = {13, 40, 20, 10, 5} p(8) = {}\nAny number invalidating the conjecture would have an infinite length sequence prefix.\n\n\nLet Sm be the set of all sequence prefixes of length m. Two sequences {a1, a2, ..., am} and {b1, b2, ..., bm} in Sm are said to belong to the same prefix family if ai < aj if and only if bi < bj for all 1 \xe2\x89\xa4 i,j \xe2\x89\xa4 m.\n\n\nFor example, in S4, {6, 3, 10, 5} is in the same family as {454, 227, 682, 341}, but not {113, 340, 170, 85}.\nLet f(m) be the number of distinct prefix families in Sm.\nYou are given f(5) = 5, f(10) = 55, f(20) = 6771.\n\n\nFind f(90).'
'''

# Solution 

# Solution Approach 
'''
'''

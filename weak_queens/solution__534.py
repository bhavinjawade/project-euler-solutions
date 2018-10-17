
# -*- coding: utf-8 -*-
'''
    File name: weak_queens\solution__534.py
    Author: Vaidic Joshi
    Date created: Oct 18, 2018
    Python Version: 3.x
'''

# Solution to Project Euler Problem #534 :: Weak Queens
# 
# For more information see:
# https://projecteuler.net/problem=534

# Problem Statement 
'''
b'The classical eight queens puzzle is the well known problem of placing eight chess queens on a 8\xc3\x978 chessboard so that no two queens threaten each other. Allowing configurations to reappear in rotated or mirrored form, a total of 92 distinct configurations can be found for eight queens. The general case asks for the number of distinct ways of placing n queens on a n\xc3\x97n board, e.g. you can find 2 distinct configurations for n=4.\n\nLets define a weak queen on a n\xc3\x97n board to be a piece which can move any number of squares if moved horizontally, but a maximum of n\xe2\x88\x921\xe2\x88\x92w squares if moved vertically or diagonally, 0\xe2\x89\xa4w<n being the "weakness factor". For example, a weak queen on a n\xc3\x97n board with a weakness factor of w=1 located in the bottom row will not be able to threaten any square in the top row as the weak queen would need to move n\xe2\x88\x921 squares vertically or diagonally to get there, but may only move n\xe2\x88\x922 squares in these directions. In contrast, the weak queen is not handicapped horizontally, thus threatening every square in its own row, independently from its current position in that row.\n\nLet Q(n,w) be the number of ways n weak queens with weakness factor w can be placed on a n\xc3\x97n board so that no two queens threaten each other. It can be shown, for example, that Q(4,0)=2, Q(4,2)=16 and Q(4,3)=256.\n\nLet $S(n)=\\displaystyle\\sum_{w=0}^{n-1} Q(n,w)$.\n\nYou are given that S(4)=276 and S(5)=3347.\n\nFind S(14).'
'''

# Solution 

# Solution Approach 
'''
'''

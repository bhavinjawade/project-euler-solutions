
# -*- coding: utf-8 -*-
'''
    File name: combined_volume_of_cuboids\solution__212.py
    Author: Vaidic Joshi
    Date created: Oct 18, 2018
    Python Version: 3.x
'''

# Solution to Project Euler Problem #212 :: Combined Volume of Cuboids
# 
# For more information see:
# https://projecteuler.net/problem=212

# Problem Statement 
'''
b'An axis-aligned cuboid, specified by parameters { (x0,y0,z0), (dx,dy,dz) }, consists of all points (X,Y,Z) such that x0 \xe2\x89\xa4 X \xe2\x89\xa4 x0+dx, y0 \xe2\x89\xa4 Y \xe2\x89\xa4 y0+dy and z0 \xe2\x89\xa4 Z \xe2\x89\xa4 z0+dz.  The volume of the cuboid is the product, dx \xc3\x97 dy \xc3\x97 dz.  The combined volume of a collection of cuboids is the volume of their union and will be less than the sum of the individual volumes if any cuboids overlap.\n\nLet C1,...,C50000 be a collection of 50000 axis-aligned cuboids such that Cn has parameters\n\nx0 = S6n-5 modulo 10000y0 = S6n-4 modulo 10000z0 = S6n-3 modulo 10000dx = 1 + (S6n-2 modulo 399)dy = 1 + (S6n-1 modulo 399)dz = 1 + (S6n modulo 399)\n\nwhere S1,...,S300000 come from the "Lagged Fibonacci Generator":\n\nFor 1 \xe2\x89\xa4 k \xe2\x89\xa4 55, Sk = [100003 - 200003k + 300007k3] \xc2\xa0 (modulo 1000000)For 56 \xe2\x89\xa4 k, Sk = [Sk-24 + Sk-55] \xc2\xa0 (modulo 1000000)\n\nThus, C1 has parameters {(7,53,183),(94,369,56)}, C2 has parameters {(2383,3563,5079),(42,212,344)}, and so on.\n\nThe combined volume of the first 100 cuboids, C1,...,C100, is 723581599.\n\nWhat is the combined volume of all 50000 cuboids, C1,...,C50000 ?'
'''

# Solution 

# Solution Approach 
'''
'''

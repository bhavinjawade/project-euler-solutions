
# -*- coding: utf-8 -*-
'''
    File name: mixtures\solution__478.py
    Author: Vaidic Joshi
    Date created: Oct 18, 2018
    Python Version: 3.x
'''

# Solution to Project Euler Problem #478 :: Mixtures
# 
# For more information see:
# https://projecteuler.net/problem=478

# Problem Statement 
'''
b'Let us consider mixtures of three substances: A, B and C. A mixture can be described by a ratio of the amounts of A, B, and C in it, i.e., (a\xc2\xa0:\xc2\xa0b\xc2\xa0:\xc2\xa0c). For example, a mixture described by the ratio (2\xc2\xa0:\xc2\xa03\xc2\xa0:\xc2\xa05) contains 20% A, 30% B and 50% C.\n\nFor the purposes of this problem, we cannot separate the individual components from a mixture. However, we can combine different amounts of different mixtures to form mixtures with new ratios.\n\nFor example, say we have three mixtures with ratios (3\xc2\xa0:\xc2\xa00\xc2\xa0:\xc2\xa02), (3\xc2\xa0:\xc2\xa06\xc2\xa0:\xc2\xa011) and (3\xc2\xa0:\xc2\xa03\xc2\xa0:\xc2\xa04). By mixing 10 units of the first, 20 units of the second and 30 units of the third, we get a new mixture with ratio (6\xc2\xa0:\xc2\xa05\xc2\xa0:\xc2\xa09), since:\n(10\xc2\xb73/5\xc2\xa0+\xc2\xa020\xc2\xb73/20\xc2\xa0+\xc2\xa030\xc2\xb73/10\xc2\xa0:\xc2\xa010\xc2\xb70/5\xc2\xa0+\xc2\xa020\xc2\xb76/20\xc2\xa0+\xc2\xa030\xc2\xb73/10\xc2\xa0:\xc2\xa010\xc2\xb72/5\xc2\xa0+\xc2\xa020\xc2\xb711/20\xc2\xa0+\xc2\xa030\xc2\xb74/10)\n= (18\xc2\xa0:\xc2\xa015\xc2\xa0:\xc2\xa027) = (6\xc2\xa0:\xc2\xa05\xc2\xa0:\xc2\xa09)\n\nHowever, with the same three mixtures, it is impossible to form the ratio (3\xc2\xa0:\xc2\xa02\xc2\xa0:\xc2\xa01), since the amount of B is always less than the amount of C.\n\nLet n be a positive integer. Suppose that for every triple of integers (a, b, c) with 0 \xe2\x89\xa4 a, b, c \xe2\x89\xa4 n and gcd(a, b, c) = 1, we have a mixture with ratio (a\xc2\xa0:\xc2\xa0b\xc2\xa0:\xc2\xa0c). Let M(n) be the set of all such mixtures.\n\nFor example, M(2) contains the 19 mixtures with the following ratios:\n{(0\xc2\xa0:\xc2\xa00\xc2\xa0:\xc2\xa01), (0\xc2\xa0:\xc2\xa01\xc2\xa0:\xc2\xa00), (0\xc2\xa0:\xc2\xa01\xc2\xa0:\xc2\xa01), (0\xc2\xa0:\xc2\xa01\xc2\xa0:\xc2\xa02), (0\xc2\xa0:\xc2\xa02\xc2\xa0:\xc2\xa01), \n(1\xc2\xa0:\xc2\xa00\xc2\xa0:\xc2\xa00), (1\xc2\xa0:\xc2\xa00\xc2\xa0:\xc2\xa01), (1\xc2\xa0:\xc2\xa00\xc2\xa0:\xc2\xa02), (1\xc2\xa0:\xc2\xa01\xc2\xa0:\xc2\xa00), (1\xc2\xa0:\xc2\xa01\xc2\xa0:\xc2\xa01), \n(1\xc2\xa0:\xc2\xa01\xc2\xa0:\xc2\xa02), (1\xc2\xa0:\xc2\xa02\xc2\xa0:\xc2\xa00), (1\xc2\xa0:\xc2\xa02\xc2\xa0:\xc2\xa01), (1\xc2\xa0:\xc2\xa02\xc2\xa0:\xc2\xa02), (2\xc2\xa0:\xc2\xa00\xc2\xa0:\xc2\xa01), \n(2\xc2\xa0:\xc2\xa01\xc2\xa0:\xc2\xa00), (2\xc2\xa0:\xc2\xa01\xc2\xa0:\xc2\xa01), (2\xc2\xa0:\xc2\xa01\xc2\xa0:\xc2\xa02), (2\xc2\xa0:\xc2\xa02\xc2\xa0:\xc2\xa01)}.\n\nLet E(n) be the number of subsets of M(n) which can produce the mixture with ratio (1 : 1 : 1), i.e., the mixture with equal parts A, B and C. \nWe can verify that E(1) = 103, E(2) = 520447, E(10)\xc2\xa0mod\xc2\xa0118 = 82608406 and E(500)\xc2\xa0mod\xc2\xa0118 = 13801403.\nFind E(10\xc2\xa0000\xc2\xa0000)\xc2\xa0mod\xc2\xa0118.'
'''

# Solution 

# Solution Approach 
'''
'''

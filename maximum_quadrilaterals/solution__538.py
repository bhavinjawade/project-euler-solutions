
# -*- coding: utf-8 -*-
'''
    File name: maximum_quadrilaterals\solution__538.py
    Author: Vaidic Joshi
    Date created: Oct 18, 2018
    Python Version: 3.x
'''

# Solution to Project Euler Problem #538 :: Maximum quadrilaterals
# 
# For more information see:
# https://projecteuler.net/problem=538

# Problem Statement 
'''
b'Consider a positive integer sequence S\xc2\xa0=\xc2\xa0(s1,\xc2\xa0s2,\xc2\xa0...,\xc2\xa0sn).\n\nLet f(S) be the perimeter of the maximum-area quadrilateral whose side lengths are 4 elements (si, sj, sk, sl) of S (all i, j, k, l distinct). If there are many quadrilaterals with the same maximum area, then choose the one with the largest perimeter.\n\nFor example, if S\xc2\xa0=\xc2\xa0(8,\xc2\xa09,\xc2\xa014,\xc2\xa09,\xc2\xa027), then we can take the elements (9,\xc2\xa014,\xc2\xa09,\xc2\xa027) and form an isosceles trapezium with parallel side lengths 14 and 27 and both leg lengths 9. The area of this quadrilateral is 127.611470879... It can be shown that this is the largest area for any quadrilateral that can be formed using side lengths from S. Therefore, f(S)\xc2\xa0=\xc2\xa09\xc2\xa0+\xc2\xa014\xc2\xa0+\xc2\xa09\xc2\xa0+\xc2\xa027\xc2\xa0=\xc2\xa059.\n\nLet un\xc2\xa0=\xc2\xa02B(3n)\xc2\xa0+\xc2\xa03B(2n)\xc2\xa0+\xc2\xa0B(n+1), where B(k) is the number of 1 bits of k in base 2.\nFor example, B(6)\xc2\xa0=\xc2\xa02, B(10)\xc2\xa0=\xc2\xa02 and B(15)\xc2\xa0=\xc2\xa04, and u5\xc2\xa0=\xc2\xa024\xc2\xa0+\xc2\xa032\xc2\xa0+\xc2\xa02\xc2\xa0=\xc2\xa027.\n\nAlso, let Un be the sequence (u1,\xc2\xa0u2,\xc2\xa0...,\xc2\xa0un).\nFor example, U10\xc2\xa0=\xc2\xa0(8,\xc2\xa09,\xc2\xa014,\xc2\xa09,\xc2\xa027,\xc2\xa016,\xc2\xa036,\xc2\xa09,\xc2\xa027,\xc2\xa028).\n\nIt can be shown that f(U5)\xc2\xa0=\xc2\xa059, f(U10)\xc2\xa0=\xc2\xa0118, f(U150)\xc2\xa0=\xc2\xa03223.\nIt can also be shown that \xce\xa3\xc2\xa0f(Un)\xc2\xa0=\xc2\xa0234761 for 4\xc2\xa0\xe2\x89\xa4\xc2\xa0n\xc2\xa0\xe2\x89\xa4\xc2\xa0150.\nFind \xce\xa3\xc2\xa0f(Un) for 4\xc2\xa0\xe2\x89\xa4\xc2\xa0n\xc2\xa0\xe2\x89\xa4\xc2\xa03\xc2\xa0000\xc2\xa0000.'
'''

# Solution 

# Solution Approach 
'''
'''

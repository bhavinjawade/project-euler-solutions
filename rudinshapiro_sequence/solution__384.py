
# -*- coding: utf-8 -*-
'''
    File name: rudinshapiro_sequence\solution__384.py
    Author: Vaidic Joshi
    Date created: Oct 18, 2018
    Python Version: 3.x
'''

# Solution to Project Euler Problem #384 :: Rudin-Shapiro sequence
# 
# For more information see:
# https://projecteuler.net/problem=384

# Problem Statement 
'''
b"Define the sequence a(n) as the number of adjacent pairs of ones in the binary expansion of n (possibly overlapping).\nE.g.: a(5) = a(1012) = 0, a(6) = a(1102) = 1, a(7) = a(1112) = 2\n\nDefine the sequence b(n) = (-1)a(n).\nThis sequence is called the Rudin-Shapiro sequence.\nAlso consider the summatory sequence of b(n): .\n\nThe first couple of values of these sequences are:\nn\xc2\xa0 \xc2\xa0 \xc2\xa0 \xc2\xa0 0 \xc2\xa0 \xc2\xa0 1 \xc2\xa0 \xc2\xa0 2 \xc2\xa0 \xc2\xa0 3 \xc2\xa0 \xc2\xa0 4 \xc2\xa0 \xc2\xa0 5 \xc2\xa0 \xc2\xa0 6 \xc2\xa0 \xc2\xa0 7\na(n) \xc2\xa0 \xc2\xa0 0 \xc2\xa0 \xc2\xa0 0 \xc2\xa0 \xc2\xa0 0 \xc2\xa0 \xc2\xa0 1 \xc2\xa0 \xc2\xa0 0 \xc2\xa0 \xc2\xa0 0 \xc2\xa0 \xc2\xa0 1 \xc2\xa0 \xc2\xa0 2\nb(n) \xc2\xa0 \xc2\xa0 1 \xc2\xa0 \xc2\xa0 1 \xc2\xa0 \xc2\xa0 1 \xc2\xa0 \xc2\xa0-1 \xc2\xa0 \xc2\xa0 1 \xc2\xa0 \xc2\xa0 1 \xc2\xa0 \xc2\xa0-1 \xc2\xa0 \xc2\xa0 1\ns(n) \xc2\xa0 \xc2\xa0 1 \xc2\xa0 \xc2\xa0 2 \xc2\xa0 \xc2\xa0 3 \xc2\xa0 \xc2\xa0 2 \xc2\xa0 \xc2\xa0 3 \xc2\xa0 \xc2\xa0 4 \xc2\xa0 \xc2\xa0 3 \xc2\xa0 \xc2\xa0 4\n\nThe sequence s(n) has the remarkable property that all elements are positive and every positive integer k occurs exactly k times.\n\nDefine g(t,c), with 1 \xe2\x89\xa4 c \xe2\x89\xa4 t, as the index in s(n) for which t occurs for the c'th time in s(n).\nE.g.: g(3,3) = 6, g(4,2) = 7 and g(54321,12345) = 1220847710.\n\nLet F(n) be the fibonacci sequence defined by:\nF(0)=F(1)=1 and\nF(n)=F(n-1)+F(n-2) for n>1.\n\nDefine GF(t)=g(F(t),F(t-1)).\n\nFind \xce\xa3GF(t) for 2\xe2\x89\xa4t\xe2\x89\xa445."
'''

# Solution 

# Solution Approach 
'''
'''

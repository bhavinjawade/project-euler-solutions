
# -*- coding: utf-8 -*-
'''
    File name: squarefree_gaussian_integers\solution__556.py
    Author: Vaidic Joshi
    Date created: Oct 18, 2018
    Python Version: 3.x
'''

# Solution to Project Euler Problem #556 :: Squarefree Gaussian Integers
# 
# For more information see:
# https://projecteuler.net/problem=556

# Problem Statement 
'''
b"A Gaussian integer is a number z\xc2\xa0=\xc2\xa0a\xc2\xa0+\xc2\xa0bi where a, b are integers and i2\xc2\xa0=\xc2\xa0-1.\nGaussian integers are a subset of the complex numbers, and the integers are the subset of Gaussian integers for which b\xc2\xa0=\xc2\xa00.\n\nA Gaussian integer unit is one for which a2\xc2\xa0+\xc2\xa0b2\xc2\xa0=\xc2\xa01, i.e. one of 1, i, -1, -i.\nLet's define a proper Gaussian integer as one for which a\xc2\xa0>\xc2\xa00 and b\xc2\xa0\xe2\x89\xa5\xc2\xa00.\n\nA Gaussian integer z1\xc2\xa0=\xc2\xa0a1\xc2\xa0+\xc2\xa0b1i is said to be divisible by z2\xc2\xa0=\xc2\xa0a2\xc2\xa0+\xc2\xa0b2i if z3\xc2\xa0=\xc2\xa0a3\xc2\xa0+\xc2\xa0b3i\xc2\xa0=\xc2\xa0z1/z2 is a Gaussian integer.\n$\\frac {z_1} {z_2} = \\frac {a_1 + b_1 i} {a_2 + b_2 i} = \\frac {(a_1 + b_1 i)(a_2 - b_2 i)} {(a_2 + b_2 i)(a_2 - b_2 i)} = \\frac {a_1 a_2 + b_1 b_2} {a_2^2 + b_2^2} + \\frac  {a_2 b_1 - a_1 b_2}  {a_2^2 + b_2^2}i = a_3 + b_3 i$\nSo, z1 is divisible by z2 if $\\frac {a_1 a_2 + b_1 b_2} {a_2^2 + b_2^2}$ and $\\frac  {a_2 b_1 - a_1 b_2}  {a_2^2 + b_2^2}$ are integers.\nFor example, 2 is divisible by 1\xc2\xa0+\xc2\xa0i because 2/(1\xc2\xa0+\xc2\xa0i)\xc2\xa0=\xc2\xa01\xc2\xa0-\xc2\xa0i is a Gaussian integer.\n\nA Gaussian prime is a Gaussian integer that is divisible only by a unit, itself or itself times a unit.\nFor example, 1\xc2\xa0+\xc2\xa02i is a Gaussian prime, because it is only divisible by 1, i, -1, -i, 1\xc2\xa0+\xc2\xa02i, i(1\xc2\xa0+\xc2\xa02i)\xc2\xa0=\xc2\xa0i\xc2\xa0-\xc2\xa02, -(1\xc2\xa0+\xc2\xa02i)\xc2\xa0=\xc2\xa0-1\xc2\xa0-\xc2\xa02i and -i(1\xc2\xa0+\xc2\xa02i)\xc2\xa0=\xc2\xa02\xc2\xa0-\xc2\xa0i.\n2 is not a Gaussian prime as it is divisible by 1\xc2\xa0+\xc2\xa0i.\n\nA Gaussian integer can be uniquely factored as the product of a unit and proper Gaussian primes.\nFor example 2\xc2\xa0=\xc2\xa0-i(1\xc2\xa0+\xc2\xa0i)2 and 1\xc2\xa0+\xc2\xa03i\xc2\xa0=\xc2\xa0(1\xc2\xa0+\xc2\xa0i)(2\xc2\xa0+\xc2\xa0i).\nA Gaussian integer is said to be squarefree if its prime factorization does not contain repeated proper Gaussian primes.\nSo 2 is not squarefree over the Gaussian integers, but 1\xc2\xa0+\xc2\xa03i is.\nUnits and Gaussian primes are squarefree by definition.\n\nLet f(n) be the count of proper squarefree Gaussian integers with a2\xc2\xa0+\xc2\xa0b2\xc2\xa0\xe2\x89\xa4\xc2\xa0n.\nFor example f(10)\xc2\xa0=\xc2\xa07 because 1, 1\xc2\xa0+\xc2\xa0i, 1\xc2\xa0+\xc2\xa02i, 1\xc2\xa0+\xc2\xa03i\xc2\xa0=\xc2\xa0(1\xc2\xa0+\xc2\xa0i)(2\xc2\xa0+\xc2\xa0i), 2\xc2\xa0+\xc2\xa0i, 3 and 3\xc2\xa0+\xc2\xa0i\xc2\xa0=\xc2\xa0-i(1\xc2\xa0+\xc2\xa0i)(1\xc2\xa0+\xc2\xa02i) are squarefree, while 2\xc2\xa0=\xc2\xa0-i(1\xc2\xa0+\xc2\xa0i)2 and 2\xc2\xa0+\xc2\xa02i\xc2\xa0=\xc2\xa0-i(1\xc2\xa0+\xc2\xa0i)3 are not.\nYou are given f(102)\xc2\xa0=\xc2\xa054, f(104)\xc2\xa0=\xc2\xa05218 and f(108)\xc2\xa0=\xc2\xa052126906.\n\nFind f(1014)."
'''

# Solution 

# Solution Approach 
'''
'''

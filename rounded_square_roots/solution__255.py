
# -*- coding: utf-8 -*-
'''
    File name: rounded_square_roots\solution__255.py
    Author: Vaidic Joshi
    Date created: Oct 18, 2018
    Python Version: 3.x
'''

# Solution to Project Euler Problem #255 :: Rounded Square Roots
# 
# For more information see:
# https://projecteuler.net/problem=255

# Problem Statement 
'''
b"We define the rounded-square-root of a positive integer n as the square root of n rounded to the nearest integer.\n\nThe following procedure (essentially Heron's method adapted to integer arithmetic) finds the rounded-square-root of n:\nLet d be the number of digits of the number n.\nIf d is odd, set $x_0 = 2 \\times 10^{(d-1)/2}$.\nIf d is even, set $x_0 = 7 \\times 10^{(d-2)/2}$.\nRepeat:\n$$x_{k+1} = \\Biggl\\lfloor{\\dfrac{x_k + \\lceil{n / x_k}\\rceil}{2}}\\Biggr\\rfloor$$\n\nuntil $x_{k+1} = x_k$.\nAs an example, let us find the rounded-square-root of n = 4321.n has 4 digits, so $x_0 = 7 \\times 10^{(4-2)/2} = 70$.\n$$x_1 = \\Biggl\\lfloor{\\dfrac{70 + \\lceil{4321 / 70}\\rceil}{2}}\\Biggr\\rfloor = 66\\\\\nx_2 = \\Biggl\\lfloor{\\dfrac{66 + \\lceil{4321 / 66}\\rceil}{2}}\\Biggr\\rfloor = 66$$\n\nSince $x_2 = x_1$, we stop here.\nSo, after just two iterations, we have found that the rounded-square-root of 4321 is 66 (the actual square root is 65.7343137\xe2\x80\xa6).\n\nThe number of iterations required when using this method is surprisingly low.\nFor example, we can find the rounded-square-root of a 5-digit integer (10,000 \xe2\x89\xa4 n \xe2\x89\xa4 99,999) with an average of 3.2102888889 iterations (the average value was rounded to 10 decimal places).\n\nUsing the procedure described above, what is the average number of iterations required to find the rounded-square-root of a 14-digit number (1013 \xe2\x89\xa4 n < 1014)?\nGive your answer rounded to 10 decimal places.\n\nNote: The symbols $\\lfloor x \\rfloor$ and $\\lceil x \\rceil$ represent the floor function and ceiling function respectively."
'''

# Solution 

# Solution Approach 
'''
'''

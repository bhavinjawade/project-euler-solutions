
# -*- coding: utf-8 -*-
'''
    File name: repeated_permutation\solution__483.py
    Author: Vaidic Joshi
    Date created: Oct 18, 2018
    Python Version: 3.x
'''

# Solution to Project Euler Problem #483 :: Repeated permutation
# 
# For more information see:
# https://projecteuler.net/problem=483

# Problem Statement 
'''
b'We define a permutation as an operation that rearranges the order of the elements {1, 2, 3, ..., n}.\nThere are n! such permutations, one of which leaves the elements in their initial order.\nFor n = 3 we have 3! = 6 permutations:\n- P1 = keep the initial order\n- P2 = exchange the 1st and 2nd elements\n- P3 = exchange the 1st and 3rd elements\n- P4 = exchange the 2nd and 3rd elements\n- P5 = rotate the elements to the right\n- P6 = rotate the elements to the left\n\n\nIf we select one of these permutations, and we re-apply the same permutation repeatedly, we eventually restore the initial order.For a permutation Pi, let f(Pi) be the number of steps required to restore the initial order by applying the permutation Pi repeatedly.For n = 3, we obtain:- f(P1) = 1 : (1,2,3) \xe2\x86\x92 (1,2,3)- f(P2) = 2 : (1,2,3) \xe2\x86\x92 (2,1,3) \xe2\x86\x92 (1,2,3)- f(P3) = 2 : (1,2,3) \xe2\x86\x92 (3,2,1) \xe2\x86\x92 (1,2,3)- f(P4) = 2 : (1,2,3) \xe2\x86\x92 (1,3,2) \xe2\x86\x92 (1,2,3)- f(P5) = 3 : (1,2,3) \xe2\x86\x92 (3,1,2) \xe2\x86\x92 (2,3,1) \xe2\x86\x92 (1,2,3)- f(P6) = 3 : (1,2,3) \xe2\x86\x92 (2,3,1) \xe2\x86\x92 (3,1,2) \xe2\x86\x92 (1,2,3)\n\n\nLet g(n) be the average value of f2(Pi) over all permutations Pi of length n.g(3) = (12 + 22 + 22 + 22 + 32 + 32)/3! = 31/6 \xe2\x89\x88 5.166666667e0g(5) = 2081/120 \xe2\x89\x88 1.734166667e1g(20) = 12422728886023769167301/2432902008176640000 \xe2\x89\x88 5.106136147e3\n\n\nFind g(350) and write the answer in scientific notation rounded to 10 significant digits, using a lowercase e to separate mantissa and exponent, as in the examples above.'
'''

# Solution 

# Solution Approach 
'''
'''

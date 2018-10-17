
# -*- coding: utf-8 -*-
'''
    File name: searching_a_triangular_array_for_a_subtriangle_having_minimumsum\solution__150.py
    Author: Vaidic Joshi
    Date created: Oct 18, 2018
    Python Version: 3.x
'''

# Solution to Project Euler Problem #150 :: Searching a triangular array for a sub-triangle having minimum-sum
# 
# For more information see:
# https://projecteuler.net/problem=150

# Problem Statement 
'''
b'In a triangular array of positive and negative integers, we wish to find a sub-triangle such that the sum of the numbers it contains is the smallest possible.\nIn the example below, it can be easily verified that the marked triangle satisfies this condition having a sum of \xe2\x88\x9242.\n\n\nWe wish to make such a triangular array with one thousand rows, so we generate 500500 pseudo-random numbers sk in the range \xc2\xb1219, using a type of random number generator (known as a Linear Congruential Generator) as follows:\nt := 0\n\nfor k = 1 up to k = 500500:\n\n\xc2\xa0 \xc2\xa0 t := (615949*t + 797807) modulo 220\n\xc2\xa0 \xc2\xa0 sk := t\xe2\x88\x92219\nThus: s1 = 273519, s2 = \xe2\x88\x92153582, s3 = 450905 etc\nOur triangular array is then formed using the pseudo-random numbers thus:\n\ns1\ns2\xc2\xa0 s3\ns4\xc2\xa0 s5\xc2\xa0 s6\xc2\xa0 \n\ns7\xc2\xa0 s8\xc2\xa0 s9\xc2\xa0 s10\n...\n\nSub-triangles can start at any element of the array and extend down as far as we like (taking-in the two elements directly below it from the next row, the three elements directly below from the row after that, and so on).\n\nThe "sum of a sub-triangle" is defined as the sum of all the elements it contains.\n\nFind the smallest possible sub-triangle sum.'
'''

# Solution 

# Solution Approach 
'''
'''

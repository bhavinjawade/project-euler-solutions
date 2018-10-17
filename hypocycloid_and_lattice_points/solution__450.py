
# -*- coding: utf-8 -*-
'''
    File name: hypocycloid_and_lattice_points\solution__450.py
    Author: Vaidic Joshi
    Date created: Oct 18, 2018
    Python Version: 3.x
'''

# Solution to Project Euler Problem #450 :: Hypocycloid and Lattice points
# 
# For more information see:
# https://projecteuler.net/problem=450

# Problem Statement 
'''
b'A hypocycloid is the curve drawn by a point on a small circle rolling inside a larger circle. The parametric equations of a hypocycloid centered at the origin, and starting at the right most point is given by:\n$x(t) = (R - r) \\cos(t) + r \\cos(\\frac {R - r} r t)$\n$y(t) = (R - r) \\sin(t) - r \\sin(\\frac {R - r} r t)$\nWhere R is the radius of the large circle and r the radius of the small circle.\n\n\nLet $C(R, r)$ be the set of distinct points with integer coordinates on the hypocycloid with radius R and r and for which there is a corresponding value of t such that $\\sin(t)$ and $\\cos(t)$ are rational numbers.\n\nLet $S(R, r) = \\sum_{(x,y) \\in C(R, r)} |x| + |y|$ be the sum of the absolute values of the x and y coordinates of the points in $C(R, r)$.\n\n\nLet $T(N) = \\sum_{R = 3}^N \\sum_{r=1}^{\\lfloor \\frac {R - 1} 2 \\rfloor} S(R, r)$ be the sum of $S(R, r)$ for R and r positive integers, $R\\leq N$  and $2r < R$.\n\n\nYou are given:C(3, 1) =\n{(3, 0), (-1, 2), (-1,0), (-1,-2)}\nC(2500, 1000) =\n{(2500, 0), (772, 2376), (772, -2376), (516, 1792),\n (516, -1792), (500, 0), (68, 504), (68, -504),(-1356, 1088), (-1356, -1088), (-1500, 1000), (-1500, -1000)}\n\nNote: (-625, 0) is not an element of C(2500, 1000) because $\\sin(t)$ is not a rational number for the corresponding values of t.\n\n\nS(3, 1) = (|3| + |0|) + (|-1| + |2|) + (|-1| + |0|) + (|-1| + |-2|) = 10\n\nT(3) = 10; T(10) = 524 ;T(100) = 580442; T(103) = 583108600.\n\n\nFind T(106).'
'''

# Solution 

# Solution Approach 
'''
'''

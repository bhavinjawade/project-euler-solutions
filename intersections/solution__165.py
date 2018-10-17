
# -*- coding: utf-8 -*-
'''
    File name: intersections\solution__165.py
    Author: Vaidic Joshi
    Date created: Oct 18, 2018
    Python Version: 3.x
'''

# Solution to Project Euler Problem #165 :: Intersections
# 
# For more information see:
# https://projecteuler.net/problem=165

# Problem Statement 
'''
b'A segment is uniquely defined by its two endpoints. By considering two line segments in plane geometry there are three possibilities: \nthe segments have zero points, one point, or infinitely many points in common.\nMoreover when two segments have exactly one point in common it might be the case that that common point is an endpoint of either one of the segments or of both. If a common point of two segments is not an endpoint of either of the segments it is an interior point of both segments.\nWe will call a common point T of two segments L1 and L2 a true intersection point of L1 and L2  if T is the only common point of L1 and L2  and T is an interior point of both segments.\n\nConsider the three segments L1, L2, and L3:\nL1: (27, 44) to (12, 32)\nL2: (46, 53) to (17, 62)\nL3: (46, 70) to (22, 40)\nIt can be verified that line segments L2 and L3 have a true intersection point. We note that as the one of the end points of L3: (22,40) lies on L1 this is not considered to be a true point of intersection. L1 and L2 have no common point. So among the three line segments, we find one true intersection point.\nNow let us do the same for 5000 line segments. To this end, we generate 20000 numbers using the so-called "Blum Blum Shub" pseudo-random number generator.\ns0 = 290797\nsn+1 = sn\xc3\x97sn (modulo 50515093)\ntn = sn (modulo 500)\nTo create each line segment, we use four consecutive numbers tn. That is, the first line segment is given by:\n(t1, t2) to (t3, t4)\nThe first four numbers computed according to the above generator should be: 27, 144, 12 and 232. The first segment would thus be (27,144) to (12,232).\nHow many distinct true intersection points are found among the 5000 line segments?'
'''

# Solution 

# Solution Approach 
'''
'''

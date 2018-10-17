
# -*- coding: utf-8 -*-
'''
    File name: crossed_lines\solution__630.py
    Author: Vaidic Joshi
    Date created: Oct 18, 2018
    Python Version: 3.x
'''

# Solution to Project Euler Problem #630 :: Crossed lines
# 
# For more information see:
# https://projecteuler.net/problem=630

# Problem Statement 
'''
b'Given a set, $L$, of unique lines, let $M(L)$ be the number of lines in the set and let $S(L)$ be the sum over every line of the number of times that line is crossed by another line in the set.  For example, two sets of three lines are shown below:\n\n\n\nIn both cases M(L) is 3 and S(L) is 6: each of the three lines is crossed by two other lines.  Note that even if the lines cross at a single point, all of the separate crossings of lines are counted.\n\n\nConsider points ($T_{2k\xe2\x88\x921}$,\xe2\x80\x89$T_{2k}$), for integer $k\xe2\x80\x89>= 1$, generated in the following way:\n\n\n$S_0 \t=  \t290797$ \n$S_{n+1} \t=  \t{S_n}^2 \\:\\: \\rm{mod} \\:\\: 50515093$\n$T_n \t=  \t(\xe2\x80\x89S_n \\:\\: \\rm{mod} \\:\\: 2000\xe2\x80\x89) \xe2\x88\x92 1000$\n\n\nFor example, the first three points are: (527,\xe2\x80\x89144), (\xe2\x88\x92488,\xe2\x80\x89732), (\xe2\x88\x92454,\xe2\x80\x89\xe2\x88\x92947).  Given the first $n$ points generated in this manner, let $L_n$ be the set of unique lines that can be formed by joining each point with every other point, the lines being extended indefinitely in both directions.  We can then define $M(L_n)$ and $S(L_n)$ as described above.\n\n\nFor example, $M(L_3) = 3$ and $S(L_3) = 6$.  Also $M(L_{100}) = 4948$ and $S(L_{100}) = 24477690$.\n\nFind $S(L_{2500})$.'
'''

# Solution 

# Solution Approach 
'''
'''

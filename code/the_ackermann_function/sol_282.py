
# -*- coding: utf-8 -*-
'''
    File name: code\the_ackermann_function\sol_282.py
    Author: Vaidic Joshi
    Date created: Oct 20, 2018
    Python Version: 3.x
'''

# Solution to Project Euler Problem #282 :: The Ackermann function
# 
# For more information see:
# https://projecteuler.net/problem=282

# Problem Statement 
'''
$\def\htmltext#1{\style{font-family:inherit;}{\text{#1}}}$

For non-negative integers $m$, $n$, the Ackermann function $A(m,n)$ is defined as follows:

$$
A(m,n) = \cases{
n+1 &$\htmltext{ if  }m=0$\cr
A(m-1,1) &$\htmltext{ if   }m>0 \htmltext{  and  } n=0$\cr
A(m-1,A(m,n-1)) &$\htmltext{ if   }m>0 \htmltext{  and  } n>0$\cr
}$$


For example $A(1,0) = 2$, $A(2,2) = 7$ and $A(3,4) = 125$.


Find $\displaystyle\sum_{n=0}^6 A(n,n)$ and give your answer mod $14^8$.
'''

# Solution 

# Solution Approach 
'''
'''

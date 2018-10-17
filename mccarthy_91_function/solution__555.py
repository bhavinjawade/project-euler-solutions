
# -*- coding: utf-8 -*-
'''
    File name: mccarthy_91_function\solution__555.py
    Author: Vaidic Joshi
    Date created: Oct 18, 2018
    Python Version: 3.x
'''

# Solution to Project Euler Problem #555 :: McCarthy 91 function
# 
# For more information see:
# https://projecteuler.net/problem=555

# Problem Statement 
'''
b'The McCarthy 91 function is defined as follows:\n$$\nM_{91}(n) = \n    \\begin{cases}\n        n - 10 & \\text{if } n > 100 \\\\\n        M_{91}(M_{91}(n+11)) & \\text{if } 0 \\leq n \\leq 100\n    \\end{cases}\n$$\n\n\nWe can generalize this definition by abstracting away the constants into new variables:\n\n$$\nM_{m,k,s}(n) = \n    \\begin{cases}\n        n - s & \\text{if } n > m \\\\\n        M_{m,k,s}(M_{m,k,s}(n+k)) & \\text{if } 0 \\leq n \\leq m\n    \\end{cases}\n$$\n\n\nThis way, we have $M_{91} = M_{100,11,10}$.\n\n\nLet $F_{m,k,s}$ be the set of fixed points of $M_{m,k,s}$. That is, \n\n$$F_{m,k,s}= \\left\\{ n \\in \\mathbb{N} \\, | \\, M_{m,k,s}(n) = n \\right\\}$$\n\n\nFor example, the only fixed point of $M_{91}$ is $n = 91$. In other words, $F_{100,11,10}= \\{91\\}$.\n \n\nNow, define $SF(m,k,s)$ as the sum of the elements in $F_{m,k,s}$ and let $S(p,m) = \\displaystyle \\sum_{1 \\leq s < k \\leq p}{SF(m,k,s)}$.\n\n\nFor example, $S(10, 10) = 225$ and $S(1000, 1000)=208724467$.\n\n\nFind $S(10^6, 10^6)$.'
'''

# Solution 

# Solution Approach 
'''
'''

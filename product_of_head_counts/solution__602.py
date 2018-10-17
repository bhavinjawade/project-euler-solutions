
# -*- coding: utf-8 -*-
'''
    File name: product_of_head_counts\solution__602.py
    Author: Vaidic Joshi
    Date created: Oct 18, 2018
    Python Version: 3.x
'''

# Solution to Project Euler Problem #602 :: Product of Head Counts
# 
# For more information see:
# https://projecteuler.net/problem=602

# Problem Statement 
'''
b"Alice enlists the help of some friends to generate a random number, using a single unfair coin. She and her friends sit around a table and, starting with Alice, they take it in turns to toss the coin. Everyone keeps a count of how many heads they obtain individually. The process ends as soon as Alice obtains a Head. At this point, Alice multiplies all her friends' Head counts together to obtain her random number.\n\n\nAs an illustration, suppose Alice is assisted by Bob, Charlie, and Dawn, who are seated round the table in that order, and that they obtain the sequence of Head/Tail outcomes THHH\xe2\x80\x94TTTT\xe2\x80\x94THHT\xe2\x80\x94H beginning and ending with Alice. Then Bob and Charlie each obtain 2 heads, and Dawn obtains 1 head. Alice's random number is therefore $2\\times 2\\times 1 = 4$.\n\n\nDefine $e(n, p)$ to be the expected value of Alice's random number, where $n$ is the number of friends helping (excluding Alice herself), and $p$ is the probability of the coin coming up Tails.\n\n\nIt turns out that, for any fixed $n$, $e(n, p)$ is always a polynomial in $p$. For example, $e(3, p) = p^3 + 4p^2 + p$.\n\n\nDefine $c(n, k)$ to be the coefficient of $p^k$ in the polynomial $e(n, p)$. So $c(3, 1) = 1$, $c(3, 2) = 4$, and $c(3, 3) = 1$.\n\n\nYou are given that $c(100, 40) \\equiv 986699437 \\text{ } (\\text{mod } 10^9+7)$.\n\n\nFind $c(10000000, 4000000) \\mod 10^9+7$."
'''

# Solution 

# Solution Approach 
'''
'''

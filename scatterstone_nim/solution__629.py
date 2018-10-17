
# -*- coding: utf-8 -*-
'''
    File name: scatterstone_nim\solution__629.py
    Author: Vaidic Joshi
    Date created: Oct 18, 2018
    Python Version: 3.x
'''

# Solution to Project Euler Problem #629 :: Scatterstone Nim
# 
# For more information see:
# https://projecteuler.net/problem=629

# Problem Statement 
'''
b"Alice and Bob are playing a modified game of Nim called Scatterstone Nim, with Alice going first, alternating turns with Bob. The game begins with an arbitrary set of stone piles with a total number of stones equal to $n$.\n\nDuring a player's turn, he/she must pick a pile having at least $2$ stones and perform a split operation, dividing the pile into an arbitrary set of $p$ non-empty, arbitrarily-sized piles where $2 \\leq p \\leq k$ for some fixed constant $k$. For example, a pile of size $4$ can be split into $\\{1, 3\\}$ or $\\{2, 2\\}$, or $\\{1, 1, 2\\}$ if $k = 3$ and in addition $\\{1, 1, 1, 1\\}$ if $k = 4$.\n\nIf no valid move is possible on a given turn, then the other player wins the game.\n\nA winning position is defined as a set of stone piles where a player can ultimately ensure victory no matter what the other player does. \n\nLet $f(n,k)$ be the number of winning positions for Alice on her first turn, given parameters $n$ and $k$. For example, $f(5, 2) = 3$ with winning positions $\\{1, 1, 1, 2\\}, \\{1, 4\\}, \\{2, 3\\}$. In contrast, $f(5, 3) = 5$ with winning positions $\\{1, 1, 1, 2\\}, \\{1, 1, 3\\}, \\{1, 4\\}, \\{2, 3\\}, \\{5\\}$.\n\nLet $g(n)$ be the sum of $f(n,k)$ over all $2 \\leq k \\leq n$. For example, $g(7)=66$ and $g(10)=291$.\n\nFind $g(200)$ mod $(10^9 + 7)$."
'''

# Solution 

# Solution Approach 
'''
'''

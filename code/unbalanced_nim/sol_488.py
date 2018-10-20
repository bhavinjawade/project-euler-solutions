
# -*- coding: utf-8 -*-
'''
    File name: code\unbalanced_nim\sol_488.py
    Author: Vaidic Joshi
    Date created: Oct 20, 2018
    Python Version: 3.x
'''

# Solution to Project Euler Problem #488 :: Unbalanced Nim
# 
# For more information see:
# https://projecteuler.net/problem=488

# Problem Statement 
'''
Alice and Bob have enjoyed playing Nim every day. However, they finally got bored of playing ordinary three-heap Nim.
So, they added an extra rule:

- Must not make two heaps of the same size.

The triple (a,b,c) indicates the size of three heaps.
Under this extra rule, (2,4,5) is one of the losing positions for the next player.

To illustrate:
- Alice moves to (2,4,3)
- Bob   moves to (0,4,3)
- Alice moves to (0,2,3)
- Bob   moves to (0,2,1)

Unlike ordinary three-heap Nim, (0,1,2) and its permutations are the end states of this game.

For an integer N, we define F(N) as the sum of a+b+c for all the losing positions for the next player, with 0 < a < b < c < N.

For example, F(8) = 42, because there are 4 losing positions for the next player, (1,3,5), (1,4,6), (2,3,6) and (2,4,5).
We can also verify that F(128) = 496062.

Find the last 9 digits of F(1018).
'''

# Solution 

# Solution Approach 
'''
'''

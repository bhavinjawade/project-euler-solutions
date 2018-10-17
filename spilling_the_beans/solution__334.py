
# -*- coding: utf-8 -*-
'''
    File name: spilling_the_beans\solution__334.py
    Author: Vaidic Joshi
    Date created: Oct 18, 2018
    Python Version: 3.x
'''

# Solution to Project Euler Problem #334 :: Spilling the beans
# 
# For more information see:
# https://projecteuler.net/problem=334

# Problem Statement 
'''
b"In Plato's heaven, there exist an infinite number of bowls in a straight line.\nEach bowl either contains some or none of a finite number of beans.\nA child plays a game, which allows only one kind of move: removing two beans from any bowl, and putting one in each of the two adjacent bowls. The game ends when each bowl contains either one or no beans.\n\nFor example, consider two adjacent bowls containing 2 and 3 beans respectively, all other bowls being empty. The following eight moves will finish the game:\n\n\n\nYou are given the following sequences:\n\n\n$\\def\\htmltext#1{\\style{font-family:inherit;}{\\text{#1}}}$\n$\n\\begin{align}\n\\qquad t_0 &= 123456,\\cr\n\\qquad t_i &= \\cases{\n\\;\\;\\frac{t_{i-1}}{2},&$\\htmltext{if }t_{i-1}\\htmltext{ is even}$\\cr\n\\left\\lfloor\\frac{t_{i-1}}{2}\\right\\rfloor\\oplus 926252,&$\\htmltext{if }t_{i-1}\\htmltext{ is odd}$\\cr}\\cr\n&\\qquad\\htmltext{where }\\lfloor x\\rfloor\\htmltext{ is the floor function }\\cr\n&\\qquad\\!\\htmltext{and }\\oplus\\htmltext{is the bitwise XOR operator.}\\cr\n\\qquad b_i &= (t_i\\bmod2^{11}) + 1.\\cr\n\\end{align}\n$\n\n\nThe first two terms of the last sequence are $b_1 = 289$ and $b_2 = 145$.\nIf we start with $b_1$ and $b_2$ beans in two adjacent bowls, $3419100$ moves would be required to finish the game.\n\nConsider now $1500$ adjacent bowls containing $b_1, b_2, \\ldots, b_{1500}$ beans respectively, all other bowls being empty. Find how many moves it takes before the game ends."
'''

# Solution 

# Solution Approach 
'''
'''

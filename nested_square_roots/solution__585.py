
# -*- coding: utf-8 -*-
'''
    File name: nested_square_roots\solution__585.py
    Author: Vaidic Joshi
    Date created: Oct 18, 2018
    Python Version: 3.x
'''

# Solution to Project Euler Problem #585 :: Nested square roots
# 
# For more information see:
# https://projecteuler.net/problem=585

# Problem Statement 
'''
b'Consider the term $\\small \\sqrt{x+\\sqrt{y}+\\sqrt{z}}$ that is representing a nested square root. $x$, $y$ and $z$ are positive integers and $y$ and $z$ are not allowed to be perfect squares, so the number below the outer square root is irrational. Still it can be shown that for some combinations of $x$, $y$ and $z$ the given term can be simplified into a sum and/or difference of simple square roots of integers, actually denesting the square roots in the initial expression. \n\nHere are some examples of this denesting:\n$\\small \\sqrt{3+\\sqrt{2}+\\sqrt{2}}=\\sqrt{2}+\\sqrt{1}=\\sqrt{2}+1$\n$\\small \\sqrt{8+\\sqrt{15}+\\sqrt{15}}=\\sqrt{5}+\\sqrt{3}$\n$\\small \\sqrt{20+\\sqrt{96}+\\sqrt{12}}=\\sqrt{9}+\\sqrt{6}+\\sqrt{3}-\\sqrt{2}=3+\\sqrt{6}+\\sqrt{3}-\\sqrt{2}$\n$\\small \\sqrt{28+\\sqrt{160}+\\sqrt{108}}=\\sqrt{15}+\\sqrt{6}+\\sqrt{5}-\\sqrt{2}$\nAs you can see the integers used in the denested expression may also be perfect squares resulting in further simplification.\n\nLet F($n$) be the number of different terms $\\small \\sqrt{x+\\sqrt{y}+\\sqrt{z}}$, that can be denested into the sum and/or difference of a finite number of square roots, given the additional condition that $0<x \\le n$. That is,\n$\\small \\displaystyle \\sqrt{x+\\sqrt{y}+\\sqrt{z}}=\\sum_{i=1}^k s_i\\sqrt{a_i}$\nwith $k$, $x$, $y$, $z$ and all $a_i$ being positive integers, all $s_i =\\pm 1$ and $x\\le n$. Furthermore $y$ and $z$  are not allowed to be perfect squares.\n\nNested roots with the same value are not considered different, for example $\\small \\sqrt{7+\\sqrt{3}+\\sqrt{27}}$, $\\small \\sqrt{7+\\sqrt{12}+\\sqrt{12}}$ and $\\small \\sqrt{7+\\sqrt{27}+\\sqrt{3}}$, that can all three be denested into $\\small 2+\\sqrt{3}$, would only be counted once.\n\nYou are given that F(10)=17, F(15)=46, F(20)=86, F(30)=213 and F(100)=2918 and F(5000)=11134074.\nFind F(5000000).'
'''

# Solution 

# Solution Approach 
'''
'''

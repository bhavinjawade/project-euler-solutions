
# -*- coding: utf-8 -*-
'''
    File name: cake_icing_puzzle\solution__566.py
    Author: Vaidic Joshi
    Date created: Oct 18, 2018
    Python Version: 3.x
'''

# Solution to Project Euler Problem #566 :: Cake Icing Puzzle
# 
# For more information see:
# https://projecteuler.net/problem=566

# Problem Statement 
'''
b'Adam plays the following game with his birthday cake.\n\nHe cuts a piece forming a circular sector of 60 degrees and flips the piece upside down, with the icing on the bottom.\nHe then rotates the cake by 60 degrees counterclockwise, cuts an adjacent 60 degree piece and flips it upside down.\nHe keeps repeating this, until after a total of twelve steps, all the icing is back on top.\n\nAmazingly, this works for any piece size, even if the cutting angle is an irrational number: all the icing will be back on top after a finite number of steps.\n\nNow, Adam tries something different: he alternates cutting pieces of size $x=\\frac{360}{9}$ degrees, $y=\\frac{360}{10}$ degrees and $z=\\frac{360 }{\\sqrt{11}}$ degrees. The first piece he cuts has size x and he flips it. The second has size y and he flips it. The third has size z and he flips it. He repeats this with pieces of size x, y and z in that order until all the icing is back on top, and discovers he needs 60 flips altogether.\n\n\n\nLet F(a, b, c) be the minimum number of piece flips needed to get all the icing back on top for pieces of size $x=\\frac{360}{a}$ degrees, $y=\\frac{360}{b}$ degrees and $z=\\frac{360}{\\sqrt{c}}$ degrees.\nLet $G(n) = \\sum_{9 \\le a < b < c \\le n} F(a,b,c)$, for integers a, b and c.\n\nYou are given that F(9,\xc2\xa010,\xc2\xa011)\xc2\xa0=\xc2\xa060, F(10,\xc2\xa014,\xc2\xa016)\xc2\xa0=\xc2\xa0506, F(15,\xc2\xa016,\xc2\xa017)\xc2\xa0=\xc2\xa0785232.\nYou are also given G(11)\xc2\xa0=\xc2\xa060, G(14)\xc2\xa0=\xc2\xa058020 and G(17)\xc2\xa0=\xc2\xa01269260.\n\nFind G(53).'
'''

# Solution 

# Solution Approach 
'''
'''

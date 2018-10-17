
# -*- coding: utf-8 -*-
'''
    File name: torpids\solution__597.py
    Author: Vaidic Joshi
    Date created: Oct 18, 2018
    Python Version: 3.x
'''

# Solution to Project Euler Problem #597 :: Torpids
# 
# For more information see:
# https://projecteuler.net/problem=597

# Problem Statement 
'''
b'The Torpids are rowing races held annually in Oxford, following some curious rules:\n\n\nA division consists of $n$ boats (typically 13), placed in order based on past performance.\n\nAll boats within a division start at 40 metre intervals along the river, in order with the highest-placed boat starting furthest upstream.\n\nThe boats all start rowing simultaneously, upstream, trying to catch the boat in front while avoiding being caught by boats behind.\n\nEach boat continues rowing until either it reaches the finish line or it catches up with ("bumps") a boat in front.\n\nThe finish line is a distance $L$ metres (the course length, in reality about 1800 metres) upstream from the starting position of the lowest-placed boat. (Because of the staggered starting positions, higher-placed boats row a slightly shorter course than lower-placed boats.)\n\nWhen a "bump" occurs, the "bumping" boat takes no further part in the race. The "bumped" boat must continue, however, and may even be "bumped" again by boats that started two or more places behind it.\n\nAfter the race, boats are assigned new places within the division, based on the bumps that occurred. Specifically, for any boat $A$ that started in a lower place than $B$, then $A$ will be placed higher than $B$ in the new order if and only if one of the following occurred:\n   $A$ bumped $B$ directly \n   $A$ bumped another boat that went on to bump $B$ \n   $A$ bumped another boat, that bumped yet another boat, that bumped $B$ \n   etc NOTE: For the purposes of this problem you may disregard the boats\' lengths, and assume that a bump occurs precisely when the two boats draw level. (In reality, a bump is awarded as soon as physical contact is made, which usually occurs when there is much less than a full boat length\'s overlap.)\n\n\nSuppose that, in a particular race, each boat $B_j$ rows at a steady speed $v_j = -$log$X_j$ metres per second, where the $X_j$ are chosen randomly (with uniform distribution) between 0 and 1, independently from one another. These speeds are relative to the riverbank: you may disregard the flow of the river.\n\n\nLet $p(n,L)$ be the probability that the new order is an even permutation of the starting order, when there are $n$ boats in the division and $L$ is the course length.\n\n\nFor example, with $n=3$ and $L=160$, labelling the boats as $A$,$B$,$C$ in starting order with $C$ highest, the different possible outcomes of the race are as follows:\n\n Bumps occurring \n   New order \n   Permutation \n   Probability \n  none \n   $A$, $B$, $C$ \n   even \n   $4/15$ \n  $B$ bumps $C$ \n   $A$, $C$, $B$ \n   odd \n   $8/45$ \n  $A$ bumps $B$ \n   $B$, $A$, $C$ \n   odd \n   $1/3$ \n  \xc2\xa0 \xc2\xa0 $B$ bumps $C$, then $A$ bumps $C$ \xc2\xa0 \xc2\xa0 \n   $C$, $A$, $B$ \n   even \n   $4/27$ \n  \xc2\xa0 \xc2\xa0 $A$ bumps $B$, then $B$ bumps $C$ \xc2\xa0 \xc2\xa0 \n   $C$, $B$, $A$ \n   odd \n   $2/27$ \n \nTherefore, $p(3,160) = 4/15 + 4/27 = 56/135$.\n\n\nYou are also given that $p(4,400)=0.5107843137$, rounded to 10 digits after the decimal point.\n\n\nFind $p(13,1800)$ rounded to 10 digits after the decimal point.'
'''

# Solution 

# Solution Approach 
'''
'''

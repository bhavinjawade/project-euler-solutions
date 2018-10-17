
# -*- coding: utf-8 -*-
'''
    File name: connectedness_of_a_network\solution__186.py
    Author: Vaidic Joshi
    Date created: Oct 18, 2018
    Python Version: 3.x
'''

# Solution to Project Euler Problem #186 :: Connectedness of a network
# 
# For more information see:
# https://projecteuler.net/problem=186

# Problem Statement 
'''
b'Here are the records from a busy telephone system with one million users:\n\nRecNrCallerCalled120000710005326001835004393600863701497.........\nThe telephone number of the caller and the called number in record n are Caller(n) = S2n-1 and Called(n) = S2n where S1,2,3,... come from the "Lagged Fibonacci Generator":\n\nFor 1 \xe2\x89\xa4 k \xe2\x89\xa4 55, Sk = [100003 - 200003k + 300007k3] (modulo 1000000)\nFor 56 \xe2\x89\xa4 k, Sk = [Sk-24 + Sk-55] (modulo 1000000)\n\nIf Caller(n) = Called(n) then the user is assumed to have misdialled and the call fails; otherwise the call is successful.\n\nFrom the start of the records, we say that any pair of users X and Y are friends if X calls Y or vice-versa. Similarly, X is a friend of a friend of Z if X is a friend of Y and Y is a friend of Z; and so on for longer chains.\n\nThe Prime Minister\'s phone number is 524287. After how many successful calls, not counting misdials, will 99% of the users (including the PM) be a friend, or a friend of a friend etc., of the Prime Minister?'
'''

# Solution 

# Solution Approach 
'''
'''

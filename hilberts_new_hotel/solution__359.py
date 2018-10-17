
# -*- coding: utf-8 -*-
'''
    File name: hilberts_new_hotel\solution__359.py
    Author: Vaidic Joshi
    Date created: Oct 18, 2018
    Python Version: 3.x
'''

# Solution to Project Euler Problem #359 :: Hilbert's New Hotel
# 
# For more information see:
# https://projecteuler.net/problem=359

# Problem Statement 
'''
b"An infinite number of people (numbered 1, 2, 3, etc.) are lined up to get a room at Hilbert's newest infinite hotel. The hotel contains an infinite number of floors (numbered 1, 2, 3, etc.), and each floor contains an infinite number of rooms (numbered 1, 2, 3, etc.). \n\n\n\nInitially the hotel is empty. Hilbert declares a rule on how the nth person is assigned a room: person n gets the first vacant room in the lowest numbered floor satisfying either of the following:\nthe floor is empty\nthe floor is not empty, and if the latest person taking a room in that floor is person m, then m + n is a perfect square\n\nPerson 1 gets room 1 in floor 1 since floor 1 is empty.\nPerson 2 does not get room 2 in floor 1 since 1 + 2 = 3 is not a perfect square.\nPerson 2 instead gets room 1 in floor 2 since floor 2 is empty.\nPerson 3 gets room 2 in floor 1 since 1 + 3 = 4 is a perfect square.\n\n\n\nEventually, every person in the line gets a room in the hotel.\n\n\n\nDefine P(f, r) to be n if person n occupies room r in floor f, and 0 if no person occupies the room. Here are a few examples:\nP(1, 1) = 1\nP(1, 2) = 3\nP(2, 1) = 2\nP(10, 20) = 440\nP(25, 75) = 4863\nP(99, 100) = 19454\n\n\n\nFind the sum of all P(f, r) for all positive f and r such that f \xc3\x97 r = 71328803586048 and give the last 8 digits as your answer."
'''

# Solution 

# Solution Approach 
'''
'''

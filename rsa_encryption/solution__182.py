
# -*- coding: utf-8 -*-
'''
    File name: rsa_encryption\solution__182.py
    Author: Vaidic Joshi
    Date created: Oct 18, 2018
    Python Version: 3.x
'''

# Solution to Project Euler Problem #182 :: RSA encryption
# 
# For more information see:
# https://projecteuler.net/problem=182

# Problem Statement 
'''
b"The RSA encryption is based on the following procedure:\nGenerate two distinct primes p and q.Compute n=pq and \xcf\x86=(p-1)(q-1).\nFind an integer e, 1<e<\xcf\x86, such that gcd(e,\xcf\x86)=1.\nA message in this system is a number in the interval [0,n-1].\nA text to be encrypted is then somehow converted to messages (numbers in the interval [0,n-1]).\nTo encrypt the text,  for each message, m, c=me mod n is calculated.\nTo decrypt the text, the following procedure is needed: calculate d such that ed=1 mod \xcf\x86, then for each encrypted message, c, calculate m=cd mod n.\nThere exist values of e and m  such that me mod n=m.We call messages m for which me mod n=m unconcealed messages.\nAn issue when choosing e is that there should not be too many unconcealed messages.  For instance, let p=19 and q=37.\nThen n=19*37=703 and \xcf\x86=18*36=648.\nIf we choose e=181, then, although gcd(181,648)=1 it turns out that all possible messagesm (0\xe2\x89\xa4m\xe2\x89\xa4n-1) are unconcealed when calculating me mod n.\nFor any valid choice of e there exist some unconcealed messages.\nIt's important that the number of unconcealed messages is at a minimum.\nChoose p=1009 and q=3643.\nFind the sum of all values of e, 1<e<\xcf\x86(1009,3643) and gcd(e,\xcf\x86)=1, so that the number of unconcealed messages for this value of e is at a minimum."
'''

# Solution 

# Solution Approach 
'''
'''

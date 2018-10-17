
# -*- coding: utf-8 -*-
'''
    File name: quadtree_encoding_a_simple_compression_algorithm\solution__287.py
    Author: Vaidic Joshi
    Date created: Oct 18, 2018
    Python Version: 3.x
'''

# Solution to Project Euler Problem #287 :: Quadtree encoding (a simple compression algorithm)
# 
# For more information see:
# https://projecteuler.net/problem=287

# Problem Statement 
'''
b'The quadtree encoding allows us to describe a 2N\xc3\x972N  black and white image as a sequence of bits (0 and 1). Those sequences are to be read from left to right like this:\nthe first bit deals with the complete 2N\xc3\x972N region;\n"0" denotes a split:\nthe current 2n\xc3\x972n region is divided into 4 sub-regions of dimension 2n-1\xc3\x972n-1,\nthe next bits contains the description of the top left, top right, bottom left and bottom right sub-regions - in that order;\n"10" indicates that the current region contains only black pixels;\n"11" indicates that the current region contains only white pixels.Consider the following 4\xc3\x974 image (colored marks denote places where a split can occur):\n\nThis image can be described by several sequences, for example :\n"001010101001011111011010101010", of length 30, or\n"0100101111101110", of length 16, which is the minimal sequence for this image.\n\nFor a positive integer N, define DN as the 2N\xc3\x972N image with the following coloring scheme:\nthe pixel with coordinates x\xe2\x80\x89=\xe2\x80\x890, y\xe2\x80\x89=\xe2\x80\x890 corresponds to the bottom left pixel,\nif (x\xe2\x80\x89-\xe2\x80\x892N-1)2\xe2\x80\x89+\xe2\x80\x89(y\xe2\x80\x89-\xe2\x80\x892N-1)2\xe2\x80\x89\xe2\x89\xa4\xe2\x80\x8922N-2 then the pixel is black,\notherwise the pixel is white.What is the length of the minimal sequence describing D24\xe2\x80\x89?'
'''

# Solution 

# Solution Approach 
'''
'''

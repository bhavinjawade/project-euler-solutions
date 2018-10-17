
# -*- coding: utf-8 -*-
'''
    File name: blood_tests\solution__352.py
    Author: Vaidic Joshi
    Date created: Oct 18, 2018
    Python Version: 3.x
'''

# Solution to Project Euler Problem #352 :: Blood tests
# 
# For more information see:
# https://projecteuler.net/problem=352

# Problem Statement 
'''
b"Each one of the 25 sheep in a flock must be tested for a rare virus, known to affect 2% of the sheep population.\nAn accurate and extremely sensitive PCR test exists for blood samples, producing a clear positive / negative result, but it is very time-consuming and expensive.\n\n\n\nBecause of the high cost, the vet-in-charge suggests that instead of performing 25 separate tests, the following procedure can be used instead:\nThe sheep are split into 5 groups of 5 sheep in each group. \nFor each group, the 5 samples are mixed together and a single test is performed. Then,\nIf the result is negative, all the sheep in that group are deemed to be virus-free.\nIf the result is positive, 5 additional tests will be performed (a separate test for each animal) to determine the affected individual(s).\n\nSince the probability of infection for any specific animal is only 0.02, the first test (on the pooled samples) for each group will be:\nNegative (and no more tests needed) with probability 0.985 = 0.9039207968.\nPositive (5 additional tests needed) with probability 1 - 0.9039207968 = 0.0960792032.\n\nThus, the expected number of tests for each group is 1 + 0.0960792032 \xc3\x97 5 = 1.480396016.\nConsequently, all 5 groups can be screened using an average of only 1.480396016 \xc3\x97 5 = 7.40198008 tests, which represents a huge saving of more than 70% !\n\n\n\nAlthough the scheme we have just described seems to be very efficient, it can still be improved considerably (always assuming that the test is sufficiently sensitive and that there are no adverse effects caused by mixing different samples). E.g.:\nWe may start by running a test on a mixture of all the 25 samples. It can be verified that in about 60.35% of the cases this test will be negative, thus no more tests will be needed. Further testing will only be required for the remaining 39.65% of the cases.\nIf we know that at least one animal in a group of 5 is infected and the first 4 individual tests come out negative, there is no need to run a test on the fifth animal (we know that it must be infected).\nWe can try a different number of groups / different number of animals in each group, adjusting those numbers at each level so that the total expected number of tests will be minimised.\n\nTo simplify the very wide range of possibilities, there is one restriction we place when devising the most cost-efficient testing scheme: whenever we start with a mixed sample, all the sheep contributing to that sample must be fully screened (i.e. a verdict of infected / virus-free must be reached for all of them) before we start examining any other animals.\n\nFor the current example, it turns out that the most cost-efficient testing scheme (we'll call it the optimal strategy) requires an average of just 4.155452 tests!\n\n\n\nUsing the optimal strategy, let T(s,p) represent the average number of tests needed to screen a flock of s sheep for a virus having probability p to be present in any individual.\nThus, rounded to six decimal places, T(25, 0.02) = 4.155452 and T(25, 0.10) = 12.702124.\n\n\n\nFind \xce\xa3T(10000, p) for p=0.01, 0.02, 0.03, ... 0.50.\nGive your answer rounded to six decimal places."
'''

# Solution 

# Solution Approach 
'''
'''

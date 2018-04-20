#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 13:07:29 2018

@author: knowledgetemple
"""

# TODO: Find the approximate or perfect square root of any number.
# What about floating-point numbers?
# The more precise the algorithm, the more iterations it'll run.

x = 0.25
guess = 0

# This constant is used to determine the root's precision.
episilon = 0.01

# Constant used to increase the guess at each iteration.
step = episilon ** 4

# The number of iterations to get to the approximate root value.
iterationsCount = 0

while abs(guess ** 2 - x) >= episilon and guess ** 2 <= x:
    iterationsCount += 1
    guess += step    

if abs(guess ** 2 - x) < episilon:
    print("The square root of " + str(x) + " is: " + str(guess))
else:
    print("Failed to find the square root of:", x)


print("Program took " + str(iterationsCount) + " iterations to find the root.")
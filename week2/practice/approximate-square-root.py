#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 13:07:29 2018

@author: knowledgetemple
"""

# TODO: Find the approximate or perfect square root of any number.
# What about floating-point numbers?
# The more precise the algorithm, the more iterations it'll run.

x = int(input("Do you want the square root of what number? "))
guess = 1

# Constant used to increase the guess at each iteration.
step = 0.001

# This constant is used to determine the root's precision.
episilon = 0.01

# The number of iterations to get to the approximate root value.
iterationsCount = 0

while guess <= x:
    iterationsCount += 1
    
    if x - guess ** 2 <= episilon:
        break
    else:
        guess += step

print("The square root of " + str(x) + " is: " + str(guess))
print("Program took " + str(iterationsCount) + " iterations to find the root.")
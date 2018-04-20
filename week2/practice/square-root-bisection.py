#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 12:43:10 2018

@author: knowledgetemple
"""

x = int(input("Enter a number: "))

minValue = 0
maxValue = x

guess = x / 2
episilon = 0.01

iterationsCount = 0

while abs(guess ** 2 - x) >= episilon:
    if guess ** 2 > x:
        maxValue = guess
    else:
        minValue = guess
        
    iterationsCount += 1
    guess = (abs(maxValue - minValue) / 2) + minValue
    
    print("Iteration number: ", iterationsCount, ", Max value: ", maxValue, ", Min Value", minValue)

print("The found root for :", x, "is:", guess)
print("Program completed with", iterationsCount, "iterations.")
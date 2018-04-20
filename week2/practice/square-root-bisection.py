#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 12:43:10 2018

@author: knowledgetemple
"""

x = int(input("Enter a number: "))

minValue = 0
maxValue = abs(x)

guess = (maxValue + minValue) / 2
episilon = 0.01

iterationsCount = 0

while abs(guess ** 2 - abs(x)) >= episilon:
    if guess ** 2 > abs(x):
        maxValue = guess
    else:
        minValue = guess
        
    iterationsCount += 1
    guess = (maxValue + minValue) / 2
    
    print("Iteration number: ", iterationsCount, ", Max value: ", maxValue, ", Min Value", minValue)

if x < 0:
    guess = -guess

print("The found root for :", x, "is:", guess)
print("Program completed with", iterationsCount, "iterations.")
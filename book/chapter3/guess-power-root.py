#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 23:10:55 2018

@author: knowledgetemple
"""

# Book chapter 3: finger exercise.
# Guesses the perfect power and root of any given number.

powerGuess = 2
rootGuess = 0

x = int(input("Enter a number: "))

while powerGuess < 6:
    rootGuess = 0
    
    while rootGuess <= x:
        if rootGuess ** powerGuess == x:
            break
        else:
            rootGuess += 1
            
    if rootGuess ** powerGuess == x:
        break
    
    powerGuess += 1

if rootGuess ** powerGuess != x:
    rootGuess = x
    powerGuess = 1

print("The root for the number " + str(x) + " is: " + str(rootGuess) + ".")
print("The power for the number " + str(x) + " is: " + str(powerGuess) + ".")
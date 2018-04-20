#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 15:08:41 2018

@author: knowledgetemple
"""

# Finger exercise - Chapter 2

# Write a program that asks the user to input 10 integers, 
# and then prints the largest odd number that was entered. 
# If no odd number was entered, 
# it should print a message to that effect.

iterations = 10
largestOddNumber = 0

while iterations != 0:
    iterations -= 1
    
    enteredNumber = int(input("Enter an odd number: "))
    
    if enteredNumber % 2 != 0 and enteredNumber > largestOddNumber:
        largestOddNumber = enteredNumber

if largestOddNumber > 0:
    print("The largest odd number is: " + str(largestOddNumber))
else:
    print("The entered numbers weren't odds.")
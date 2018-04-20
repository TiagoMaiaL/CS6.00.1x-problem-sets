#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 13:15:38 2018

@author: knowledgetemple
"""

high = 100
low = 0

guess = int((high + low) / 2)

print("Please think of a number between 0 and 100!")

while True:
    print("Is your secret number " + str(guess) + "?")
    hint = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    
    if hint == "h":
        high = guess
    elif hint == "l":
        low = guess
    elif hint == "c":
        break
    else:
        print("Sorry, I did not understand your input.")
        continue
    
    guess = int((high + low) / 2)

print("Game over. Your secret number was: " + str(guess))

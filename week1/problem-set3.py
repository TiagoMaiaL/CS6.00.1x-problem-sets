#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 13:16:47 2018

@author: knowledgetemple
"""

s = "azcbobobegghakl"

longestSubstring = ""
currentSubstring = ""

alphabet = "abcdefghijklmnopqrstuvwxyz"

for letter in s:
    lastSubstringLetter = ""
    
    if len(currentSubstring) > 0:
        lastSubstringLetter = currentSubstring[len(currentSubstring) - 1]
    
    LetterOrder = 0
    substringLetterOrder = 0
    
    for index in range(0, len(alphabet)):
        alphabetLetter = alphabet[index]
        
        if alphabetLetter == letter:
            letterOrder = index
            
        if alphabetLetter == lastSubstringLetter:
            substringLetterOrder = index
    
    if len(currentSubstring) == 0 or letterOrder >= substringLetterOrder:
        currentSubstring += letter
        
        if len(currentSubstring) > len(longestSubstring):
            longestSubstring = currentSubstring
        
    else:
        currentSubstring = letter

print("Longest substring in alphabetical order is: " + longestSubstring)
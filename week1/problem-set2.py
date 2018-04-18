#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 08:40:42 2018

@author: knowledgetemple
"""

s = "azcbobobegghakl"

occurrencesCount = 0
searchLetterIndex = 0
searchedWord = "bob"

for index in range(len(s)):
    letter = s[index]
    
    if letter == searchedWord[searchLetterIndex]:
        searchLetterIndex += 1
        
        if searchLetterIndex >= len(searchedWord):
            occurrencesCount += 1
            
            if letter == searchedWord[0]:
                searchLetterIndex = 1
            else:
                searchLetterIndex = 0
                
    elif letter == searchedWord[0]:
        searchLetterIndex = 1
    else:
        searchLetterIndex = 0

print("Number of times bob occurs is: " + str(occurrencesCount))
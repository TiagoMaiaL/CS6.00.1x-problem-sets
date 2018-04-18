#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 23:35:55 2018

@author: knowledgetemple
"""

s = "azcbobobegghakl"
vowelsCount = 0


for letter in s:
    if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
        vowelsCount += 1


print("Number of vowels:", vowelsCount)
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 23:35:55 2018

@author: knowledgetemple
"""

s = "azcbobobegghakl"
vowelsCount = 0


for word in s:
    if word == "a" or word == "e" or word == "i" or word == "o" or word == "u":
        vowelsCount += 1


print("Number of vowels:", vowelsCount)
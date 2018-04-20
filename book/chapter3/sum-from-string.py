#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 10:23:06 2018

@author: knowledgetemple
"""

s = "1.23,2.4,3.123"
result = 0

for char in s:
    for numberChar in "0123456789":
        if numberChar == char:
            result += int(char)

print("The result is: " + str(result))
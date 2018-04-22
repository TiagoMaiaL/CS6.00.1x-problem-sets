#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 21 13:10:56 2018

@author: knowledgetemple
"""

def multiply(a, b):
    if b == 1:
        return a
    else:
        b -= 1
        return a + multiply(a, b)
    
def factorial(n):
    if n == 1:
        return n
    else:
        return multiply(n, factorial(n - 1))

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 21 21:56:57 2018

@author: knowledgetemple
"""

def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    minValue = min(a, b)
    greatestDivisor = 1
    
    while minValue > 1:
        if a % minValue == 0 and b % minValue == 0:
            greatestDivisor = minValue
            break
        else:
            minValue -= 1
    
    return greatestDivisor

def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    
    if b == 0:
        return a
    else:
        minValue = min(a, b)
        maxValue = max(a, b)
        
        return gcdRecur(minValue, maxValue % minValue)
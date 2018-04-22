#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 09:05:20 2018

@author: knowledgetemple
"""

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    
    if len(aStr) == 0:
        return False
    
    elif len(aStr) == 1:
        return aStr == char

    
    middleIndex = int(len(aStr) / 2)
    middleChar = aStr[middleIndex]
            
    if middleChar == char:
        return True    
    
    elif middleChar > char:
        return isIn(char, aStr[0:middleIndex])
        
    else:
        return isIn(char, aStr[middleIndex + 1:-1])

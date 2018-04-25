#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 22:17:22 2018

@author: knowledgetemple
"""

def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''    
    oddTuple = ()
    for i in range(len(aTup)):
        if i % 2 == 0:
            oddTuple += (aTup[i],)
    
    return oddTuple

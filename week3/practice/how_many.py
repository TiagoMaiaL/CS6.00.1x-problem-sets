#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 14:16:11 2018

@author: knowledgetemple
"""

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    count = 0
    
    for value in aDict.values():
        count += len(value)

    return count

print(how_many(animals))

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    biggest = max(map(len, aDict.values()))
    biggestKey = ''
    
    for key in aDict:
        if len(aDict[key]) == biggest:
            biggestKey = key
            break
    
    return biggestKey

print('biggest:', biggest(animals))
    
    
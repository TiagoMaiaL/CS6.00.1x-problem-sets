#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 12:19:06 2018

@author: knowledgetemple
"""

def isPalindrome(word):
    '''
    word: string, the word to be checked.
    
    returns: True if the word is a palindrome, False otherwise.
    '''
    if len(word) <= 1:
        return True
    else:
        return word[0] == word[-1] and isPalindrome(word[1:-1])
    
word = 'doggod'
print(isPalindrome(word))
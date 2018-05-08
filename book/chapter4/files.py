#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 13:27:43 2018

@author: knowledgetemple
"""

# Working with files to save computations.

nameHandle = open('testing.txt', 'w')

for i in range(2):
    name = input('Enter a name: ')
    nameHandle.write(name + '\n')
    
nameHandle.close()

nameHandle = open('testing.txt', 'r')

for line in nameHandle:
    print(line)

nameHandle.close()
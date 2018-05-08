#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 10:20:15 2018

@author: knowledgetemple
"""

# Understanding scopes in Python

def f(x):
    def g():
        #x = 'abc'
        print('x =', x)
    
    def h():
        z = x
        print('z =', z)
    
    x = x + 11
    print('x =', x)
    h()
    g()
    print('x =', x)
    
    return g
    
x = 3
z = f(x)
print('x =', x)
print('z =', z)
z()

def i():
    print(y)

def e():
    print(y)
    y = 1
    
y = 3
i()

y = 3
e()
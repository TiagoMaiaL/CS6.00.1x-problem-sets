#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 21 17:51:02 2018

@author: knowledgetemple
"""

def genPrimes():
    primes = []
    guess = 1
    
    while True:
        guess += 1
        isPrime = True
        
        for p in primes:
            if guess % p == 0:
                isPrime = False
                break

        if isPrime:
            primes.append(guess)
            yield guess
        else:
            continue
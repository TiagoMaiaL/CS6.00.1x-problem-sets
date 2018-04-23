#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 17:36:46 2018

@author: knowledgetemple
"""

balance = 999999
annualInterestRate = 0.18

def getMinimumMonthlyPayment(initialBalance, annualInterestRate):
    '''
    initialBalance: float, the outstanding credit card balance at the first month.
    annualInterestRate: float, the interest to be applied yearly
    
    returns: the minimum montly constant amount necessary to pay the debt in a year.
    '''

    monthlyInterestRate = annualInterestRate / 12.0
    
    lowerBound = initialBalance / 12.0
    upperBound = initialBalance * ((1 + monthlyInterestRate) ** 12) / 12.0
    
    guess = (lowerBound + upperBound) / 2
    
    while True:
        remainingBalance = initialBalance
        
        for month in range(12):            
            remainingBalance -= guess
            remainingBalance = remainingBalance + remainingBalance * (annualInterestRate / 12.0)
            
        if abs(remainingBalance) <= 0.01:
            break
        else:
            if remainingBalance < 0:
                upperBound = guess
            else:
                lowerBound = guess
            
            guess = (lowerBound + upperBound) / 2
    
    return guess
    
lowestPayment = getMinimumMonthlyPayment(balance, annualInterestRate)
print('Lowest Payment:', round(lowestPayment, 2))
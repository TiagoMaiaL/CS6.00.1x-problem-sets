#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 12:35:40 2018

@author: knowledgetemple
"""

balance = 3926
annualInterestRate = 0.2

def getMinimumMonthlyPayment(initialBalance, annualInterestRate):
    '''
    initialBalance: float, the outstanding credit card balance at the first month.
    annualInterestRate: float, the interest to be applied yearly
    
    returns: the minimum montly constant amount necessary to pay the debt in a year.
    '''

    guess = 10
    
    while guess <= initialBalance:
        remainingBalance = initialBalance        
        
        for month in range(12):
            remainingBalance -= guess
            remainingBalance = remainingBalance + remainingBalance * (annualInterestRate / 12.0)
        
        if remainingBalance < 0:
           break
       
        else:
            guess += 10
            
    return guess
    
print('Lowest Payment:', getMinimumMonthlyPayment(balance, annualInterestRate))    

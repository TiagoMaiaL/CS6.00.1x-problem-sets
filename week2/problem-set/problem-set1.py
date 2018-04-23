#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 11:07:05 2018

@author: knowledgetemple
"""

balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

def getRemainingAnnualBalance(initialBalance, annualInterestRate, monthlyPaymentRate, currentMonth = 12):
    '''
    initialBalance: float, the outstanding credit card balance at the first month.
    annualInterestRate: float
    montlyPaymentRate: float, the minimum amount to be applied and removed from the balance at each month.
    
    returns: the remakning balance at the end of a year.
    '''
    if currentMonth == 0:
        return balance - balance * monthlyPaymentRate
    else:
        remainingBalance = getRemainingAnnualBalance(initialBalance, annualInterestRate, monthlyPaymentRate, currentMonth - 1)

        # applies the montly interest        
        remainingBalance += remainingBalance * (annualInterestRate / 12.0)
        
        # if the month is not the final one, applies the minimum payment.
        if currentMonth != 12:
            remainingBalance -= remainingBalance * monthlyPaymentRate
        
        return remainingBalance

remainingBalance = getRemainingAnnualBalance(balance, annualInterestRate, monthlyPaymentRate)
print('Remaining balance:', round(remainingBalance, 2))
    
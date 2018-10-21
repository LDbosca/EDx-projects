#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""

def guesser(balance, annualInterestRate, lowerBound, upperBound):
    """Finds the lowest monthly payment required to pay off a credit card where interest is
    compounded monthly using bisection search.
    """ 
    testBalance = balance
    epsilon = 0.1
    monthlyPayment = (lowerBound + upperBound)/2
    for month in range(0,12):
     testBalance = testBalance - monthlyPayment
     testBalance = (testBalance * (annualInterestRate/12.0)) + testBalance
    if abs(testBalance) <= epsilon:
        print("Lowest Payment: " + str(round(monthlyPayment, 2)))         
    elif testBalance < 0:
        upperBound = monthlyPayment
        guesser(balance, annualInterestRate, lowerBound, upperBound)
    elif testBalance > epsilon:
        lowerBound = monthlyPayment
        guesser(balance, annualInterestRate, lowerBound, upperBound)
        
def call_guesser(balance, annualInterestRate):
    """ Calls guesser function.
    
    Takes as input balance, the balance on the credit card at the start of the year (a number)
    and the annual interest rate as a decimal"""
    monthlyInterestRate = annualInterestRate/12
    upperBound = (balance * (1 + monthlyInterestRate)**12)/12
    lowerBound = balance/12
    return guesser(balance, annualInterestRate, lowerBound, upperBound)
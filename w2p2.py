#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Finds lowest monthly payment to pay off credit card balance. Uses brute force enumeration
and works in steps of 10.
"""

balance = float(input("Please enter the credit card balance: "))
annualInterestRate = float(input("Please enter the annual interest rate as a deciaml: "))

def guesser(balance, annualInterestRate, monthlyPayment):
    for month in range(0,12):
     balance = balance - monthlyPayment
     balance = round(balance * (annualInterestRate/12.0), 2) + balance
    if balance <= 0:
        print("Lowest payment: " + str(monthlyPayment))
        return monthlyPayment
    else:
        return False

x = 0
while guesser(balance, annualInterestRate, x) == False:
    x += 10
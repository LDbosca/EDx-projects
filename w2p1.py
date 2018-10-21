#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Calculates credit card balance after one year if only the minimum monthly payment is made.

nalance == outstanding balance on the credit card
annualInterestRate == annual interest rate as a decimal
monthlyPaymentRate == minimum monthly payment rate as a decimal
"""
balance = int(input("Please enter the balance: "))
annualInterestRate = float(input("Please enter the annual interest rate: "))
monthlyPaymentRate = float(input("Please enter the monthlyPaymentRate: "))


for month in range(0,12):
     minPayment = round(balance * monthlyPaymentRate, 2)
     balance = balance - minPayment
     balance = round(balance * (annualInterestRate/12.0), 2) + balance
         
print(round(balance, 2))
     
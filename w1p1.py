#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Program to count the number of vowels in string s
"""
s = input("Please enter a string: ")
ans = 0
for letter in s:
    if letter == "a" or letter == "e" or letter =="i" \
    or letter == "o" or letter == "u":
        ans += 1     
print(ans)
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Counts occurences of "bob" in string s
"""
s = input("Please enter a string: ")
ans = 0
m = 0
n = 3
for letter in s:
    if s[m:n] == "bob":
        ans += 1
        m += 1
        n += 1
    else:
        m += 1
        n += 1
print("Number of times bob occurs is: " + str(ans)) 
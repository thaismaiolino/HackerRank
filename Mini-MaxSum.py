# Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.

# Input Format

# A single line of five space-separated integers.

# Constraints

# Each integer is in the inclusive range .
# Output Format

# Print two space-separated long integers denoting the respective minimum and maximum values that can be calculated by summing exactly four of the five integers. (The output can be greater than a 32 bit integer.)

# Sample Input

# 1 2 3 4 5
# Sample Output

# 10 14



#!/bin/python

import sys

arr = map(int, raw_input().strip().split(' '))
n = 4

temp = arr[:]
maximus = []
minimus = []
while n>0:
    maximus.append(max(arr))
    arr.remove(max(arr))
    minimus.append(min(temp))
    temp.remove(min(temp))
    n = n-1

print sum(minimus),sum(maximus)


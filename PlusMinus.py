# Given an array of integers, calculate the fractions of its elements that are positive, negative, and are zeros. Print the decimal value of each fraction on a new line.

# Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, though answers with absolute error of up to  are acceptable.

# Input Format

# The first line contains an integer, , denoting the size of the array. 
# The second line contains  space-separated integers describing an array of numbers .

# Output Format

# You must print the following  lines:

# A decimal representing of the fraction of positive numbers in the array compared to its size.
# A decimal representing of the fraction of negative numbers in the array compared to its size.
# A decimal representing of the fraction of zeros in the array compared to its size.
# Sample Input

# 6
# -4 3 -9 0 4 1         
# Sample Output

# 0.500000
# 0.333333
# 0.166667



#!/bin/python

import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))

zero = 0.00
positive = 0.00
negative = 0.00
for item in arr:
    if item < 0.00:
        negative = float(negative+1)
    elif item > 0.00:
        positive= float(positive+1)
    else:
        zero=float(zero+1)
print float(positive/n)
print float(negative/n)
print float(zero/n)
# Given an array of integers, find the sum of its elements.

# Complete the simpleArraySum function which takes  arguments, an integer  and an integer array  and returns an integer denoting the sum of all array elements.

# Raw Input Format

# The first line contains an integer, , denoting the size of the array. 
# The second line contains  space-separated integers representing the array's elements.

# Sample Input 0

# 6
# 1 2 3 4 10 11
# Sample Output 0

# 31


#!/bin/python

import sys

def simpleArraySum(n, ar):
    # Complete this function
    return sum(ar)

n = int(raw_input().strip())
ar = map(int, raw_input().strip().split(' '))
result = simpleArraySum(n, ar)
print(result)


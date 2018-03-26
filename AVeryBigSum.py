# Calculate and print the sum of the elements in an array, keeping in mind that some of those integers may be quite large.

# Complete the function aVeryBigSum which takes  arguments, an integer  and a long integer array  and returns a long integer denoting the sum of all array elements.

# Constraints



# Raw Input Format

# The first line of the input consists of an integer . 
# The next line contains  space-separated integers contained in the array.

# Sample Input 0

# 5
# 1000000001 1000000002 1000000003 1000000004 1000000005
# Sample Output 0

# 5000000015


#!/bin/python

import sys

def aVeryBigSum(n, ar):
    # Complete this function
    return sum(ar)

n = int(raw_input().strip())
ar = map(long, raw_input().strip().split(' '))
result = aVeryBigSum(n, ar)
print(result)


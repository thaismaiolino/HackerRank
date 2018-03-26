# Colleen is having a birthday! She will have a cake with one candle for each year of her age. When she blows out the candles, she’ll only be able to blow out the tallest ones.

# Find and print the number of candles she can successfully blow out.

# Input Format

# integer

# Colleen's age 

#  space-separated integers

# candle heights 

# Output Format

# Print the number of candles Colleen blows out.

# Sample Input 0

# 4
# 3 2 1 3
# Sample Output 0

# 2



#!/bin/python

import sys

def birthdayCakeCandles(n, ar):
    # Complete this function
    max_height = max(ar)
    counter = 0
    for item in ar:
        if item == max_height:
            counter = counter+1
    return counter
            
n = int(raw_input().strip())
ar = map(int, raw_input().strip().split(' '))
result = birthdayCakeCandles(n, ar)
print(result)
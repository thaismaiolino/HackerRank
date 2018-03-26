# Given a square matrix, calculate the absolute difference between the sums of its diagonals.

# Complete the diagonalDifference function which takes a  integer array as a parameter and return an integer denoting the absolute difference between the diagonal sums.

# Constraints


# Raw Input Format

# The first line contains a single integer,  denoting the number of rows and columns in the matrix . 
# The next  lines denote the matrix 's rows, with each line containing  space-separated integers describing the columns.

# Sample Input 0

# 3
# 11 2 4
# 4 5 6
# 10 8 -12
# Sample Output 0

# 15



#!/bin/python

import sys


n = int(raw_input().strip())
a = []
diagonal_sum = 0
secondary_diagonal_sum = 0
index_i = 0
index_j = n-1
for a_i in xrange(n):
    a_temp = map(int,raw_input().strip().split(' '))
    a.append(a_temp)    
for idx_i, i in enumerate(a):
    for idx_j, j in enumerate(i):
        if idx_i==idx_j and index_i == idx_i and index_j == idx_j  :
            diagonal_sum = diagonal_sum + j
            secondary_diagonal_sum = secondary_diagonal_sum + j
            index_i = index_i+1
            index_j = index_j-1
        elif idx_i==idx_j:
            diagonal_sum = diagonal_sum + j
        elif index_i == idx_i and index_j == idx_j :
            secondary_diagonal_sum = secondary_diagonal_sum + j
            index_i = index_i+1
            index_j = index_j-1
            
print abs(diagonal_sum - secondary_diagonal_sum)
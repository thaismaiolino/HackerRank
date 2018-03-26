# Alice and Bob each created one problem for HackerRank. A reviewer rates the two challenges, awarding points on a scale from  to  for three categories: problem clarity, originality, and difficulty.

# We define the rating for Alice's challenge to be the triplet , and the rating for Bob's challenge to be the triplet .

# Your task is to find their comparison points by comparing  with ,  with , and  with .

# If , then Alice is awarded  point.
# If , then Bob is awarded  point.
# If , then neither person receives a point.
# Comparison points is the total points a person earned.

# Given  and , can you compare the two challenges and print their respective comparison points?

# Input Format

# The first line contains  space-separated integers, , , and , describing the respective values in triplet . 
# The second line contains  space-separated integers, , , and , describing the respective values in triplet .

# Constraints



# Output Format

# Print two space-separated integers denoting the respective comparison points earned by Alice and Bob.

# Sample Input

# 5 6 7
# 3 6 10
# Sample Output

# 1 1 




#!/bin/python

import sys

def solve(a0, a1, a2, b0, b1, b2):
    # Complete this function
    A = [a0,a1,a2]
    B = [b0,b1,b2]
    pointsA = 0
    pointsB = 0
    for valA, valB  in zip(A,B):
        if valA > valB:
            pointsA += 1
        elif valB > valA:
            pointsB += 1
    return pointsA, pointsB
    
a0, a1, a2 = raw_input().strip().split(' ')
a0, a1, a2 = [int(a0), int(a1), int(a2)]
b0, b1, b2 = raw_input().strip().split(' ')
b0, b1, b2 = [int(b0), int(b1), int(b2)]
result = solve(a0, a1, a2, b0, b1, b2)
print " ".join(map(str, result))


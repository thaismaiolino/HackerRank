# Consider a staircase of size :

#    #
#   ##
#  ###
# ####
# Observe that its base and height are both equal to , and the image is drawn using # symbols and spaces. The last line is not preceded by any spaces.

# Write a program that prints a staircase of size .

# Input Format

# A single integer, , denoting the size of the staircase.

# Output Format

# Print a staircase of size  using # symbols and spaces.

# Note: The last line must have  spaces in it.

# Sample Input

# 6 
# Sample Output

#      #
#     ##
#    ###
#   ####
#  #####
# ######




#!/bin/python

import sys


n = int(raw_input().strip())
temp = n
while temp >0:
    repeat_space = temp-1
    repeat_hashtag = n - repeat_space
    print " "*repeat_space + "#"*repeat_hashtag
    temp = temp-1
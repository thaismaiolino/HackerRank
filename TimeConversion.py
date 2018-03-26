# Given a time in -hour AM/PM format, convert it to military (24-hour) time.

# Note: Midnight is 12:00:00AM on a 12-hour clock, and 00:00:00 on a 24-hour clock. Noon is 12:00:00PM on a 12-hour clock, and 12:00:00 on a 24-hour clock.

# Complete the timeConversion function which takes 1 argument, a string s and returns a string denoting the 24-hr formatted time.

# Raw Input Format

# A single string  containing a time in -hour clock format (i.e.:  or ), where  and .

# Sample Input 0

# 07:05:45PM
# Sample Output 0

# 19:05:45




#!/bin/python

import sys

def timeConversion(s):
    # Complete this function

    if "PM" in s:
        if ("12:" != s[:3]):
            hour = int(s[:2]) + 12
            return str(hour)+s[2:-2]
        else:
            return s[:-2]
    if "AM" in s:
        if ("12:" == s[:3]):
            return "00"+s[2:-2]
        else:
            return s[:-2]
        
s = raw_input().strip()
result = timeConversion(s)
print(result)


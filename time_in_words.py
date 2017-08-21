# python solution for The Time in Words
# https://www.hackerrank.com/challenges/the-time-in-words/problem
# by tinotk

import sys

timestr = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen",
         "fourteen", "quarter", "sixteen", "seventeen", "eighteen", "nineteen","twenty","thirty","forty","fifty"]

def mm(n):
    if n >= 50:
        return timestr[22] + ("" if not n%50 else " "+timestr[n % 50-1])
    elif n == 15 or n == 45:
        return "quarter"
    elif n==30:
        return "half"
    elif n >=40:
        return timestr[21] + ("" if not n%40 else " "+timestr[n % 40-1])
    elif n >= 30:
        return timestr[20] + ("" if not n%30 else " "+timestr[n % 30-1])
    elif n >= 20:
        return timestr[19]+ ("" if not n%20 else " "+timestr[n % 20-1])
    else:
        return timestr[n-1]

h = int(input().strip())
m = int(input().strip())

if m==0:
    print(timestr[h-1]+" o' clock")
elif m <= 30:
    if m == 15 or m == 30:
        print(mm(m)+" past "+timestr[h-1])
    else:
        print(mm(m)+(" minute past " if m == 1 else " minutes past " )+timestr[h-1])
else:
    if m == 45:
        print(mm(m) + " to " + timestr[h])
    else:
        print(mm(60-m)+(" minute to " if 60-m == 1 else " minutes to " )+timestr[h])
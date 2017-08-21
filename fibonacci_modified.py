# Python solution for Fibonacci Modified
# https://www.hackerrank.com/challenges/fibonacci-modified/problem
# by tinotk

import sys

#iterative bottom up
def mod_fib(n):
    for i in range(2,n):
        dp.append(dp[i - 2] + dp[i - 1]**2)
    return dp[n-1]
'''
top-down approach
def mod_fib2(n):
    dp = [0]*10000
    dp[1]=1 #a manual
    dp[2]=2 #b
    if dp[n]>0:
        return dp[n]
    else:
        dp[n] = mod_fib2(n-2) + mod_fib2(n-1)**2
    return dp[n]
'''
dp = []
a,b,n = input().split()
dp.extend([int(a),int(b)])
print(mod_fib(int(n)))
#print(mod_fib2(int(n)))
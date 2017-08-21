'''
https://www.hackerrank.com/challenges/coin-change/problem
'''

# C: set of coins value, n: change amount
def getWays(C,n):
    m = len(C)
    dp = [[0 for x in range(m)] for x in range(n+1)]
    for i in range(m):
        dp[0][i] = 1 # only 1 way to make change of 0
    for i in range(1,n+1):
        for j in range(m):
            x = dp[i - C[j]][j] if i - C[j] >= 0 else 0
            y = dp[i][j-1] if j >= 1 else 0
            dp[i][j] = x+y
   # print(dp)
    return dp[n][m-1]

if __name__ == "__main__":
    n,m = input().strip().split()
    n, m = [int(n), int(m)]
    c = list(map(int, input().strip().split(' ')))
    print(getWays(c,n))

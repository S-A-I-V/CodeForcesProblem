import math

MOD = 10**9 + 7

def expected_median(n, k, a):
    ones = a.count(1)
    zeros = n - ones
    dp = [[0]*(k+1) for _ in range(ones+1)]
    dp[0][0] = 1
    for i in range(1, ones+1):
        for j in range(min(i, k)+1):
            dp[i][j] = (dp[i-1][j-1] + dp[i-1][j]) % MOD
    total = 0
    for i in range((k+1)//2, min(ones, k)+1):
        total += dp[ones][i] * dp[zeros][k-i]
        total %= MOD
    return total

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    print(expected_median(n, k, a))
    
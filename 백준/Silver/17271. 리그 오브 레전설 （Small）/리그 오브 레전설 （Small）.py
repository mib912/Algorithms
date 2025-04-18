import sys
input = sys.stdin.readline
mod = 1000000007

n, m = map(int, input().split())

dp = [1] * (n+1)

for i in range(m, n+1):
    dp[i] = (dp[i-1] + dp[i-m]) % mod

print(dp[n])
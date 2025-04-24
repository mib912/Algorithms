import sys
input = sys.stdin.readline

n, k = map(int, input().split())
inf = 1e7
dp = [inf] * (n+1)
dp[0] = 0

for i in range(n):
    if i <= n:
        dp[i+1] = min(dp[i+1], dp[i]+1)
    if i+i//2 <= n:
        dp[i+i//2] = min(dp[i+i//2], dp[i]+1)

if dp[n] <= k:
    print("minigimbob")
else:
    print("water")
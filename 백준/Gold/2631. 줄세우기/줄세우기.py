import sys
input = sys.stdin.readline

n = int(input())
lines = []
for _ in range(n):
    lines.append(int(input()))

dp = [1] * n
for i in range(n):
    for j in range(i):
        if lines[j] < lines[i]:
            dp[i] = max(dp[i], dp[j]+1)
print(n-max(dp))
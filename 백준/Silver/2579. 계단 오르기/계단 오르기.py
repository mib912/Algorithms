
import sys
input = sys.stdin.readline

n = int(input())
scores = [0]
for _ in range(n):
    scores.append(int(input()))

dp = [0] * (n+1)
dp[1] = scores[1]

if n > 1:
    dp[2] = scores[1] + scores[2]
for i in range(3, n+1):
    dp[i] = max(dp[i-3]+scores[i-1]+scores[i], dp[i-2]+scores[i]) # 도착지점에서 한칸 아래에서 올라온 경우, 두칸 아래에서 올라온 경우로 나누어 생각하는게 더 쉬움

print(dp[n])
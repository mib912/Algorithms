import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * (n+1)  # dp[i] = i일까지 일 했을 때 벌 수 있는 최대 이익

for i in range(1, n+1):
    t, p = map(int, input().split())
    dp[i] = max(dp[i-1], dp[i])  # 이전일 최대이익과 비교

    if i+t <= n+1:  # n=7이면 8일차에 퇴사
        dp[i+t-1] = max(dp[i-1]+p, dp[i+t-1])  # i+t-1 = 당일도 포함
print(dp[-1])
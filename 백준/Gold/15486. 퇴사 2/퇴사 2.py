import sys
input = sys.stdin.readline

n = int(input())
ls = [list(map(int, input().split())) for _ in range(n)]
dp = [0] * (n+1)  # dp[i] = i일까지 일 했을 때 벌 수 있는 최대 이익

profit = 0
for i in range(n):
    profit = max(dp[i], profit)
    if i + ls[i][0] > n:  # 퇴사일 넘어갔을 경우
        continue

    dp[i+ls[i][0]] = max(profit+ls[i][1], dp[i+ls[i][0]])  # i일에 상담했을 경우
print(max(dp))
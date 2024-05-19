import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

n = int(input())
dp = [i for i in range(n+1)] # 1로 표현할 수 있는 개수로 dp 초기화

for i in range(1, n+1):
    for j in range(1, i):
        if j*j > i: # 작거나 같은 제곱수의 합으로 나타내야 함
            break
        if dp[i] > dp[i-j*j] + 1:
            dp[i] = dp[i-j*j] + 1

print(dp[n])
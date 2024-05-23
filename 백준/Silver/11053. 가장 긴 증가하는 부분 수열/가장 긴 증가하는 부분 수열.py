import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))

dp = [1 for _ in range(n)]  # dp[i] = A[i]를 마지막 값으로 갖는 가장 긴 부분증가수열의 길이

for i in range(1, n):
    for j in range(i):
        if A[i] > A[j]:  # 이전값 보다 크고
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))
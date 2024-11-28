import sys
input = sys.stdin.readline

n = int(input())
S = list(map(int, input().split()))
reversedS = list(reversed(S))

incDp = [1] * n
decDp = [1] * n
dp = [0] * n
for i in range(n):
    for j in range(i):
        if S[i] > S[j]:
            incDp[i] = max(incDp[i], incDp[j]+1)

        if reversedS[i] > reversedS[j]:
            decDp[i] = max(decDp[i], decDp[j] + 1)

decDp = decDp[::-1]
for i in range(n):
    dp[i] = incDp[i] + decDp[i] - 1

print(max(dp))
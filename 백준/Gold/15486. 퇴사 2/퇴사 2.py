import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
n = int(input())
schedule = [list(map(int, input().split())) for _ in range(n)]
dp = [-1] * (n+1)

def recur(cur):
    global res
    if cur > n:
        return -1234567890
    if cur == n:
        return 0
    if dp[cur] != -1:
        return dp[cur]
    dp[cur] = max(recur(cur+1), recur(cur+schedule[cur][0])+schedule[cur][1])
    return dp[cur]

print(recur(0))
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

n, k = map(int, input().split())
ls = [list(map(int, input().split())) for _ in range(n)]

dp = [[-1] * 100001 for _ in range(n)]
def recur(cur, w):
    if w > k:
        return -1234567890
    if cur == n:
        return 0
    if dp[cur][w] != -1:
        return dp[cur][w]
    
    dp[cur][w] = max(recur(cur+1,w), recur(cur+1,w + ls[cur][0]) + ls[cur][1])
    return dp[cur][w]

print(recur(0,0))
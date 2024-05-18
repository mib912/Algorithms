import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

n = int(input())
costs = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1]*3 for _ in range(n)]

def recur(cur, prev): # 현재 cur번 집을 색칠해야하고, 마지막에 prev색으로 색칠했을때 앞으로 색칠할때 최소 비용
    if cur == n:
        return 0
    if dp[cur][prev] != -1:
        return dp[cur][prev]

    ret = int(1e9)
    for i in range(3):
        if i == prev:
            continue
        ret = min(ret, recur(cur+1, i) + costs[cur][i])
    dp[cur][prev] = ret
    return dp[cur][prev]

print(recur(0,-1))
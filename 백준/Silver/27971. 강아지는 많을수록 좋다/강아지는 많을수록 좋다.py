import sys
from collections import deque

input = sys.stdin.readline

n,m,a,b = map(int, input().split())
dp = [0] * (n+1)
visited = [False] * (n+1)

for _ in range(m):
    l,r = map(int, input().split())
    for i in range(l, r+1):
        visited[i] = True # 닫힌구간 방문처리

dp[n] = 0
q = deque()
q.append(n)
while q:
    value = q.popleft()
    if value == 0:
        break
    for i in (value-a, value-b):
        if i >= 0:
            if visited[i]:
                continue
            else:
                q.append(i)
                dp[i] = dp[value] + 1
                visited[i] = True

if dp[0]:
    print(dp[0])
else:
    print(-1)
            


# 11724 연결 요소의 개수

import sys
from collections import deque

sys.setrecursionlimit(10**7) # 재귀 호출 시 런타임 에러 발생 방지
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[0]*(n+1) for _ in range(n+1)]

for _ in range(m):
    u,v = map(int, input().split())
    graph[u][v] = 1
    graph[v][u] = 1

# bfs
def bfs(v):
    que = deque([v])
    visited2[v] = True
    
    while que:
        v = que.popleft()
        for i in range(1, n+1):
            if not visited2[i] and graph[v][i] == 1:
                que.append(i)
                visited2[i] = True
    
cnt = 0
visited2 = [False] * (n+1)

for i in range(1, n+1):
    if not visited2[i]:
        cnt += 1
        bfs(i)

print(cnt)
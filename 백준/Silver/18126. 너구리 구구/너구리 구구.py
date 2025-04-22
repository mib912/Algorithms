# 18126 너구리 구구

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

n = int(input())
graph = [[] for _ in range(n+1)]

visited = [False] * (n+1)
dist = [0] * (n+1)

for _ in range(n-1):
    a,b,c = map(int, input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])

def dfs(v):
    visited[v] = True
    for i, d in graph[v]:
        if not visited[i]:
            dist[i] = d + dist[v]
            dfs(i)
    return

dfs(1)
print(max(dist))
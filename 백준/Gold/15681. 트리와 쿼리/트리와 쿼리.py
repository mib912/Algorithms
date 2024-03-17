from collections import deque
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n,r,q = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)

for _ in range(n-1):
    u,v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(v):
    visited[v] = 1
    for i in graph[v]:
        if visited[i] == 0:
            dfs(i)
            visited[v] += visited[i]

dfs(r)

for _ in range(q):
    u = int(input())
    print(visited[u])
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m, r = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
seq = 1 # 방문순서

def dfs(r):
    global seq
    visited[r] = seq
    graph[r].sort()
    for i in graph[r]:
        if visited[i] == 0:
            seq += 1
            dfs(i)

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

dfs(r)
for i in range(1, n+1):
    print(visited[i])
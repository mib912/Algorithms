
from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

n, m, r = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
seq = 1
que = deque()

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


def bfs(r):
    global seq
    visited[r] = seq
    seq += 1
    que = [r]
    while que:
        q = que.pop(0)
        graph[q].sort()
        for i in graph[q]:
            if visited[i] == 0:
                visited[i] = seq
                seq += 1
                que.append(i)


bfs(r)
for i in range(1, n+1):
    print(visited[i])

from collections import deque
import sys
input = sys.stdin.readline

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [0] * (n+1)
visited = [False] * (n+1)
answer = []

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

def bfs(v):
    que = deque()
    que.append(v)
    visited[v] = True

    while que:
        now = que.popleft()
        for i in graph[now]:
            if not visited[i]: # 방문하지 않음
                visited[i] = True
                distance[i] = distance[now] + 1
                que.append(i)
                if distance[i] == k:
                    answer.append(i)

bfs(x)

if len(answer) == 0:
    print(-1)

else:
    answer.sort()
    for i in answer:
        print(i, end='\n')
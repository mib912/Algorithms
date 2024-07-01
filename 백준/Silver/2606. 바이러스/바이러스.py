import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
answer = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(cur):
    global answer
    visited[cur] = True
    answer += 1

    for nxt in graph[cur]:
        if visited[nxt]:
            continue
        dfs(nxt)

dfs(1)
print(answer-1)
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

n = int(input())
a, b = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
flag = False # 촌수 찾았는지 확인

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(v, count):
    global flag
    visited[v] = True

    if v == b:
        flag = True
        print(count)

    for i in graph[v]:
        if not visited[i]:
            dfs(i, count+1)

dfs(a, 0)
if flag == False:
    print(-1)
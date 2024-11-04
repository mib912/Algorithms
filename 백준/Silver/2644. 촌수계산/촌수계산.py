import sys
input = sys.stdin.readline

n = int(input())
a, b = map(int, input().split())
m = int(input())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
flag = False # 촌수 찾았는지 확인

for _ in range(m):
    x,y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(v, cnt):
    global flag
    visited[v] = True

    if v == b:
        flag = True
        print(cnt)

    for i in graph[v]:
        if visited[i] == False:
            dfs(i, cnt + 1)    

dfs(a, 0)
if flag == False:
    print(-1)
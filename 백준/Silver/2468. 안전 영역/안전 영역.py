# 2468 안전 영역

import sys
from collections import deque

sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n = int(input())
graph = []
maxNum = 0
for _ in range(n):
    graph.append(list(map(int, input().split())))
    maxNum = max(maxNum, max(graph[-1]))

def bfs(x,y,num):
    que = deque()
    que.append((x,y))
    visited[x][y] = True

    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    while que:
        a,b = que.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if visited[nx][ny] or graph[nx][ny] <= num:
                continue
            que.append((nx,ny))
            visited[nx][ny] = True
    

result = 0
for m in range(maxNum):
    cnt = 0
    visited = [[False]*n for _ in range(n)] # 비 한번 계산할 때마다 reset 되어야 하기 떄문
    for i in range(n):
        for j in range(n):
            if graph[i][j] > m and visited[i][j] == False:
                bfs(i,j,m)
                cnt += 1
    result = max(result, cnt)
print(result)


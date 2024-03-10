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

def dfs(x,y,num): # num은 maxNum
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        if visited[nx][ny] and graph[nx][ny] <= num:
            continue
        if not visited[nx][ny] and graph[nx][ny] > num:
            visited[nx][ny] = True
            dfs(nx,ny,num)


result = 0
for m in range(maxNum):
    cnt = 0
    visited = [[False]*n for _ in range(n)] # 비 한번 계산할 때마다 reset 되어야 하기 떄문
    for i in range(n):
        for j in range(n):
            if graph[i][j] > m and visited[i][j] == False:
                dfs(i,j,m)
                cnt += 1
    result = max(result, cnt)
print(result)


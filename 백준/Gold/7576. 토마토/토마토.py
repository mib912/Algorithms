# 7576 토마토
# 최소 날짜 구하라 > bfs 이용

import sys
from collections import deque

sys.setrecursionlimit(10**7)
input = sys.stdin.readline

m,n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

que = deque() # 익은 토마토가 들어있는 위치
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            que.append((i,j))

def bfs():
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    while que:
        x, y = que.popleft()    
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 상하좌우에 익지 않은 토마토가 있다면
            if 0<=nx<n and 0<=ny<m and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1 # +1 씩 해주면서 몇번째날 해당 토마토가 익었는지 알 수 있음
                que.append((nx,ny))

bfs()

# bfs 종료 후
result = 0
for tomato in graph:
    for t in tomato:
        if t == 0: # 익지 않은 토마토가 존재
            print(-1)
            exit()
    else: # 한줄(행)씩 가장 큰 값을 찾아 마지막에 익은 토마토 찾음
        result = max(result, max(tomato))
print(result - 1) # 처음 시작이 1이기 떄문에 -1 
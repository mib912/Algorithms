import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().rstrip())) for _ in range(n)]
result = []
cnt = 0

dx = [0,0,1,-1]
dy = [1,-1,0,0]

# dfs
def dfs(x,y):
    global cnt # 전역변수 cnt 사용
    
    if x < 0 or x >= n or y < 0 or y >= n:
        return
    if graph[x][y] == 1:
        cnt += 1
        graph[x][y] = 0 # 방문한 곳으로 처리
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            dfs(i,j)
            result.append(cnt)
            cnt = 0

result.sort()
print(len(result)) # 총 단지수 
for k in result: # 각 단지마다 집의 수
    print(k)
import sys
from collections import deque

sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def dfs(x,y,number):
    if len(number) == 6:
        result.add(number)
        return
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if nx < 0 or nx >= 5 or ny < 0 or ny >= 5:
            continue
        dfs(nx,ny,number+graph[nx][ny])


graph = [list(map(str, input().split())) for _ in range(5)]
result = set()
for i in range(5):
    for j in range(5):
        dfs(i,j,graph[i][j])
print(len(result))
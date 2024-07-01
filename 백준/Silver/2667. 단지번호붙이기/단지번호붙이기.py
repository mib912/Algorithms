import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

n = int(input())
graph = [list(map(int, input().rstrip())) for _ in range(n)]
cnt = 0
result = []

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def dfs(x,y):
    global cnt
    
    if x < 0 or x >= n or y < 0 or y >= n:
        return
    if graph[x][y] == 1:
        graph[x][y] = 0 # 방문처리
        cnt += 1 # 단지내 집의 수 count

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)

# 1인 경우에만 방문
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            dfs(i,j)
            result.append(cnt)
            cnt = 0

result.sort()
print(len(result))
for k in result:
    print(k)
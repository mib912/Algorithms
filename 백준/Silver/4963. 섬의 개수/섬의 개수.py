import sys
sys.setrecursionlimit(10**7)

input = sys.stdin.readline

dx = [1,-1,0,0,1,1,-1,-1]
dy = [0,0,1,-1,1,-1,1,-1]

def dfs(x,y):
    if x < 0 or x >= h or y < 0 or y >= w:
        return
    
    if graph[x][y] == 1:
        graph[x][y] = 0  # 방문처리

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx,ny)

while True:
    answer = 0
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    
    graph = [list(map(int, input().split())) for _ in range(h)]
    
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                dfs(i,j)
                answer += 1
    print(answer)
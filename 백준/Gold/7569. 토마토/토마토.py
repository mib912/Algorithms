from collections import deque
import sys
input = sys.stdin.readline

m,n,h = map(int, input().split())
tomato = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
# for _ in range(h):
#     for _ in range(n):
#         tomato.append(list(map(int, input().split())))

days = 0
dx = [1,-1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dz = [0,0,0,0,1,-1]
visited = [[[False] * m for _ in range(n)] for _ in range(h)]
que = deque()

def bfs():
    while que:
        x,y,z = que.popleft()

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if nx < 0 or nx >= h or ny < 0 or ny >= n or nz < 0 or nz >= m:
                continue
            if tomato[nx][ny][nz] == 0 and visited[nx][ny][nz] == False:
                que.append((nx,ny,nz))
                tomato[nx][ny][nz] = tomato[x][y][z] + 1
                visited[nx][ny][nz] = True

for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomato[i][j][k] == 1 and visited[i][j][k] == False:
                que.append((i,j,k))
                visited[i][j][k] = True

bfs()
flag = True
for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomato[i][j][k] == 0:
                flag = False
            days = max(days,tomato[i][j][k])

if flag:
    print(days-1)
else:
    print(-1)
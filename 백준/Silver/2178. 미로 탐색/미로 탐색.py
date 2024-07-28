from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().rstrip())) for _ in range(n)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(x,y):
    q = deque()
    q.append((x,y))

    while q:
        a,b = q.popleft()

        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]

            if 0 <= nx < n and 0 <= ny < m and  graph[nx][ny] == 1:
                q.append((nx, ny))
                graph[nx][ny] = graph[a][b] + 1
    
    return graph[n-1][m-1]

print(bfs(0,0))
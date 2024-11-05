from collections import deque
import sys
input = sys.stdin.readline

dx = [1,2,2,1,-1,-2,-2,-1]
dy = [2,1,-1,-2,-2,-1,1,2]
n = int(input())

def bfs(x,y,moveX,moveY):
    global answer

    que = deque()
    que.append([x,y])
    graph[x][y] = 1
    while que:
        a, b = que.popleft()

        if a == moveX and b == moveY:
            return graph[a][b] - 1
        for i in range(8):
            nx = a + dx[i]
            ny = b + dy[i]

            if nx < 0 or nx >= l or ny < 0 or ny >= l:
                continue
            if graph[nx][ny] == 0:
                que.append([nx,ny])
                graph[nx][ny] = graph[a][b] + 1


for _ in range(n):
    l = int(input())
    graph = [[0] * l for _ in range(l)]

    x, y = map(int, input().split())
    moveX, moveY = map(int, input().split())

    if x == moveX and y == moveY:
        print(0)
        continue

    answer = bfs(x, y, moveX, moveY)
    print(answer)




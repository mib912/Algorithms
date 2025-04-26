import sys
input = sys.stdin.readline

n = int(input())
max_answer = -float("inf")
min_answer = float("inf")

dx = [1,0]
dy = [0,1]

def dfs(x, y, route, sign):
    global max_answer, min_answer
    if x == n-1 and y == n-1:
        answer = eval(''.join(route))
        min_answer = min(answer, min_answer)
        max_answer = max(answer, max_answer)
        return

    for i in range(2):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
            visited[nx][ny] = True
            if sign: # 부호가 나올 차례
                dfs(nx, ny, route+graph[nx][ny], False)
            else: # 숫자가 나올 차례
                dfs(nx, ny, "(" + route + graph[nx][ny] + ")", True)
            visited[nx][ny] = False


graph = [list(input().strip().split()) for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]
visited[0][0] = True

dfs(0,0,graph[0][0], True)

print(max_answer, min_answer)
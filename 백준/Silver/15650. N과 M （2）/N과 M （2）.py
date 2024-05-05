import sys

input = sys.stdin.readline

n,m = map(int, input().split())

selected = [0] * m
visited = [False] * (n+1)

def recur(cur, start):
    if cur == m:
        print(*selected)
        return
    for i in range(start, n+1):
        if visited[i]:
            continue
        selected[cur] = i
        visited[i] = True
        recur(cur+1, i+1)
        visited[i] = False

recur(0, 1)

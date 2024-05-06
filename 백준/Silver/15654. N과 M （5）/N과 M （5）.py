import sys

input = sys.stdin.readline

n,m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

selected = [0] * m
visited = [False] * 10001
def recur(cur):
    if cur == m:
        print(*selected)
        return
    for i in range(n):
        if visited[arr[i]]:
            continue
        selected[cur] = arr[i]
        visited[arr[i]] = True
        recur(cur+1)
        visited[arr[i]] = False

recur(0)
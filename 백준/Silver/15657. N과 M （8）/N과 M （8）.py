import sys
input = sys.stdin.readline

n,m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

selected = [0] * m
def recur(cur, start):
    if cur == m:
        print(*selected)
        return
    for i in range(start, n):
        selected[cur] = arr[i]
        recur(cur+1, i)

recur(0,0)
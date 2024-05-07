import sys

input = sys.stdin.readline

while True:
    arr = list(map(int, input().split()))
    k = arr[0]
    if k == 0:
        break
    nums = arr[1:]

    selected = [0] * 6
    visited = [False] * k

    def recur(cur, start):
        if cur == 6:
            print(*selected)
            return
        for i in range(start, k):
            if visited[i]:
                continue
            selected[cur] = nums[i]
            visited[i] = True
            recur(cur+1, i)
            visited[i] = False

    recur(0, 0)
    print()
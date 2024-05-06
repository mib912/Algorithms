import sys

input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))

result = []
selected = []
visited = [False] * n
def recur(depth):
    global res

    if depth == n:
        result.append(sum(abs(selected[i]-selected[i+1]) for i in range(n-1)))
        return

    for i in range(n):
        if visited[i]:
            continue
        selected.append(A[i])
        visited[i] = True
        recur(depth+1)
        visited[i] = False
        selected.pop()

recur(0)
print(max(result))
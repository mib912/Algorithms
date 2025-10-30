import sys
from itertools import permutations
input = sys.stdin.readline

a, b = input().split()
b = int(b)
digits = list(a)

n = len(digits)
visited = [False] * n  # a의 각 인덱스의 숫자 사용여부
max_val = -1


def backtrack(depth, cur):
    global max_val

    if depth == n:
        if cur[0] == '0':
            return
        if int(cur) < b:
            max_val = max(max_val, int(cur))
        return

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            backtrack(depth+1, cur+digits[i])
            visited[i] = False


backtrack(0, "")
print(max_val)
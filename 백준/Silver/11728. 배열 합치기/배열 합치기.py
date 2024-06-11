# 11728 배열합치기
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
ls = []
a, b = 0, 0
while a < n or b < m:
    if a == n:  # A배열 다 합친 후 B배열 값 append
        ls.append(B[b])
        b += 1
    elif b == m:
        ls.append(A[a])
        a += 1
    else:
        if A[a] < B[b]:
            ls.append(A[a])
            a += 1
        else:
            ls.append(B[b])
            b += 1

print(*ls)
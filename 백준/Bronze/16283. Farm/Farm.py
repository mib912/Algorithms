
import sys

input = sys.stdin.readline

a,b,n,w = map(int, input().split())
answer = []

for i in range(1,n):
    if a*i + b*(n-i) == w:
        answer.append([i, n-i])
if len(answer) == 1:
    print(*answer[0])
else:
    print(-1)
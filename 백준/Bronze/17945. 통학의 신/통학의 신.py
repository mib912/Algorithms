import sys

input = sys.stdin.readline

a,b = map(int, input().split())
answer = set()
for i in range(-1000,1001):
    if i**2 + 2*a*i + b == 0:
        answer.add(i)
print(*sorted(answer))
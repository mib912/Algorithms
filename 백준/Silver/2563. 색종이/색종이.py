import sys

input = sys.stdin.readline

n = int(input())

paper = [[0] * 100 for _ in range(100)]

for _ in range(n):
    x,y = map(int, input().split())
    for a in range(x,x+10):
        for b in range(y,y+10):
            paper[b][a] = 1

result = 0
for box in paper:
    result += box.count(1)
print(result)
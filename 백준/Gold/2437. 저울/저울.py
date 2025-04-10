import sys
input = sys.stdin.readline

n = int(input())
weights = list(map(int, input().split()))

weights.sort()

target = 1
for w in weights:
    if target < w:
        break
    target += w

print(target)
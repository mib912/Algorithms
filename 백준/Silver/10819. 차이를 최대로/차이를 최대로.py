
import sys
from itertools import permutations

n = int(input())
A = list(map(int, input().split()))

res = 0
perm = permutations(A)

for p in perm:
    tmp = 0
    for i in range(n-1):
        tmp += abs(p[i] - p[i+1])
    res = max(res, tmp)

print(res)
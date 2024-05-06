import sys
from itertools import combinations

input = sys.stdin.readline

N,L,R,X = map(int, input().split())
levels = list(map(int, input().split()))

cnt = 0
for i in range(1,N+1):
    comb = combinations(levels, i)
    
    for x in comb:
        if sum(x) >= L and sum(x) <= R and max(x)-min(x) >= X:
            cnt += 1
print(cnt)
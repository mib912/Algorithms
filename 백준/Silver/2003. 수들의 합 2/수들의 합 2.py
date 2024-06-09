import sys
input = sys.stdin.readline

n, m = map(int, input().split())
ls = list(map(int, input().split()))
answer = 0

s,e = 0,1
while s <= n and e <= n:
    tmp = sum(ls[s:e])
    if tmp == m:
        answer += 1
        s += 1
    elif tmp > m:
        s += 1
    else:
        e += 1
print(answer)
import sys
input = sys.stdin.readline

n = int(input())
cnt = 0


for a in range(2,n):
    for b in range(1,n):
        for c in range(1,n):
            if c -b < 2:
                continue
            if a % 2 == 1:
                continue
            if a + b + c == n:
                cnt += 1
print(cnt)
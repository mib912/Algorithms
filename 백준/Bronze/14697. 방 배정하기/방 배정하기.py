import sys

input = sys.stdin.readline

A,B,C,n = map(int, input().split())
flag = False
for a in range(n//A+1):
    for b in range(n//B+1):
        for c in range(n//C+1):
            if a * A + b * B + c * C == n:
                flag = True
                break
if flag:
    print(1)
else:
    print(0)
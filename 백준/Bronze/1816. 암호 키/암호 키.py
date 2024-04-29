import sys

input = sys.stdin.readline

n = int(input())
flag = False

for _ in range(n):
    num = int(input())
    flag = False
    for i in range(2, 1000001):
        if num % i == 0:
            flag = True
            print("NO")
            break
    if not flag:
        print("YES")
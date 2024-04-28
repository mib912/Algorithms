import sys

input = sys.stdin.readline

arr = list(map(int, input().split()))

for i in range(min(arr),1000001):
    cnt = 0
    for j in arr:
        if i % j == 0:
            cnt += 1
    if cnt >= 3:
        print(i)
        break
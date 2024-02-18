import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
arr = list(map(int, input().split()))

start, end = 0, n-1
arr.sort()
answer = 0
while end > start:
    if arr[start] + arr[end] < m:
        start += 1
    elif arr[start] + arr[end] > m:
        end -= 1
    else:
        answer += 1
        start += 1
        end -= 1
print(answer)
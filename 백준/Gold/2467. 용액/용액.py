import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

start,end = 0,n-1
answer = float('inf')
while end > start:
    tot = arr[start]+arr[end]
    if abs(tot) < answer:
        answer = abs(tot)
        left = start
        right = end
    else:
        if tot == 0:
            break
        elif tot < 0:
            start += 1
        else:
            end -= 1
print(arr[left], arr[right])
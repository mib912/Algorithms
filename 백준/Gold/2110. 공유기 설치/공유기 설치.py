import sys
input = sys.stdin.readline

n, c = map(int, input().split())
arr = [int(input()) for _ in range(n)]
arr.sort()

s = 1 # 집 간의 최소거리
e = arr[-1] - arr[0] # 집 간의 최대거리
ans = 0

while s <= e:
    mid = (s+e)//2 # 최대거리
    cnt = 1 # 처음집에 공유기 설치
    cur = arr[0] # 현재 위치
    for i in range(1, n):
        if arr[i] - cur >= mid:
            cnt += 1
            cur = arr[i]
    if cnt >= c:
        s = mid+1
        ans = max(ans, mid)
    else:
        e = mid-1
print(ans)
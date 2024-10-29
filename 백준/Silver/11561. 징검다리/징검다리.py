import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    start = 0
    end = n
    result = 0
    while start <= end:
        mid = (start+end) // 2 # 밟을 수 있는 징검다리 수
        if mid * (mid+1) // 2 <= n:
            start = mid + 1
            result = mid
        else:
            end = mid - 1
    print(result)
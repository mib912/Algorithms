import sys
input = sys.stdin.readline

n, m = map(int, input().split())
trees = list(map(int, input().split()))

start = 0
end = max(trees)
answer = 0 # 절단기 높이
while start <= end:
    mid = (start + end) // 2
    total = 0
    for t in trees:
        if t > mid:
            total += t - mid
    
    if total >= m:
        start = mid + 1
        answer = mid
    else:
        end = mid - 1

print(answer)
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
trees = list(map(int, input().split()))
trees.sort()

s = 1
e = trees[-1]

while s <= e:
    total = 0
    mid = (s+e)//2
    for t in trees:
        if t > mid:
            total += (t - mid)
    if total >= m:
        s = mid+1
    else:  # 높이를 낮춰야 함
        e = mid-1
print(e)  # 높이의 최댓값
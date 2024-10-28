import sys
input = sys.stdin.readline

x, y = map(int, input().split())
prevZ = y * 100 // x
result = 0

if prevZ >= 99:
    result = -1
else:
    start = 0
    end = x
    while start <= end:
        mid = (start+end) // 2
        z = (y+mid)*100 // (x+mid)
        if z > prevZ:
            result = mid
            end = mid - 1
        else:
            start = mid + 1

print(result)
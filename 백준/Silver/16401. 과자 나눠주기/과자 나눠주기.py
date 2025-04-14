import sys
input = sys.stdin.readline

m, n = map(int, input().split())
snack = sorted(list(map(int, input().split())))

start = 1
end = snack[-1]

answer = 0
while start <= end:
    mid = (start + end) // 2

    cnt = 0 # 길이가 mid인 것을 만들 수 있는 개수
    for s in snack:
        cnt += s // mid
        
    if cnt >= m:
        answer = mid
        start = mid + 1
    else:
        end = mid - 1
print(answer)
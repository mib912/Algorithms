import sys

input = sys.stdin.readline

n, m = map(int, input().split())
box = [list(map(int, input().rstrip())) for _ in range(n)]

size = min(n,m) # 최대 정사각형 한변의 크기는 size를 넘기지 못함
answer = 1
for i in range(n):
    for j in range(m):
        for k in range(size, 0, -1):
            if i+k-1 < n and j+k-1 < m:
                if box[i][j] == box[i][j+k-1] and box[i][j] == box[i+k-1][j] and box[i][j] == box[i+k-1][j+k-1]:
                    answer = max(answer, k**2)

print(answer)
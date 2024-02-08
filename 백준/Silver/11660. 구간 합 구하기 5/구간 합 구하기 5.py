import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

sumArr = [[0]*(n+1) for _ in range(n+1)]
# 누적합
for i in range(1,n+1):
    for j in range(1, n+1):
        sumArr[i][j] = sumArr[i-1][j] + sumArr[i][j-1] - sumArr[i-1][j-1] + arr[i-1][j-1]

for _ in range(m):
    x,y,a,b = map(int, input().split()) # (x,y)부터 (a,b)까지의 부분합
    partSum = sumArr[a][b] - sumArr[x-1][b] - sumArr[a][y-1] + sumArr[x-1][y-1]
    print(partSum)
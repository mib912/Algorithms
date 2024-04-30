import sys

input = sys.stdin.readline

n, k = map(int, input().split())
info = []
str = []
dex = []

for _ in range(n):
    s, d, i = map(int, input().split())
    info.append([s, d, i])

for i in range(n):
    str.append(info[i][0])
    dex.append(info[i][1])

info.sort(key=lambda x: x[2])

answer = int(1e9)
for s in str:
    for d in dex:
        int = 0
        cnt = 0
        for i in range(n):
            if info[i][0] <= s and info[i][1] <= d:
                cnt += 1
                int = info[i][2]
            if cnt == k:
                break
        if cnt == k:
            answer = min(answer, s+d+int)
print(answer)
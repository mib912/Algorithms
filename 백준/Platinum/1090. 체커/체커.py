import sys

input = sys.stdin.readline

n = int(input())
graph = []
X = []
Y = []

for _ in range(n):
    x, y = map(int, input().split())
    graph.append([x, y])
    X.append(x)
    Y.append(y)

answer = [1e9] * n
# 각 좌표에 대한 최소 점으로부터의 거리 계산
for i in X:  # 입력 받은 x값에 관한 모든 점들이 교점이 될 수 있음
    for j in Y:  # 입력 받은 y값에 관한 모든 점들이 교점이 될 수 있음
        dist = []
        for a, b in graph:
            dist.append(abs(i - a) + abs(j - b))
        dist.sort()
        temp = 0
        for d in range(n):
            temp += dist[d]
            answer[d] = min(answer[d], temp)
print(*answer)
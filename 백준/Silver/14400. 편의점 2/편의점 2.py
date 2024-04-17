import sys

input = sys.stdin.readline

n = int(input())
graph = []
result = 0

for _ in range(n):
    x, y = map(int, input().split())
    graph.append([x, y])

graph.sort(key=lambda x: x[0])
xPos = graph[(n-1)//2][0]
graph.sort(key=lambda x: x[1])
yPos = graph[(n-1)//2][1]

for i in range(n):
    result += abs(graph[i][0] - xPos)
    result += abs(graph[i][1] - yPos)

print(result)
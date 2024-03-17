import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

n = int(input())
nodes = [[] for _ in range(n+1)]
visited = [0] * (n+1) # 부모를 담을 변수
for _ in range(n-1):
    a, b = map(int, input().split())
    nodes[a].append(b)
    nodes[b].append(a)

queue = deque()
queue.append(1)
def bfs():
    while queue:
        now = queue.popleft()
        for i in nodes[now]:
            if visited[i] == 0:
                visited[i] = now
                queue.append(i)
bfs()

for i in range(2,n+1):
    print(visited[i])
import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())

graph = [[] * (n+1) for _ in range(n+1)]
visited = [False] * (n+1)
distance = [INF] * (n+1)


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, node = heapq.heappop(q)

        if distance[node] < dist:  # 이미 방문한 적 있음
            continue
        # 큐에서 뽑아낸 노드의 인접노드 탐색
        for next in graph[node]:
            # 시작 -> node 거리 + node -> node의 인접노드 거리
            cost = distance[node] + next[1]
            if cost < distance[next[0]]:  # cost < 시작 -> node의 인접노드 거리
                distance[next[0]] = cost
                heapq.heappush(q, (cost, next[0]))


for _ in range(m):
    s, e, c = map(int, input().split())
    graph[s].append((e, c))

start, end = map(int, input().split())
dijkstra(start)
print(distance[end])
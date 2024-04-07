import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

V,E,P = map(int, input().split())
graph = [[] for _ in range(V+1)]
distance = [INF] * (V+1)

for _ in range(E):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, node = heapq.heappop(q)
        if distance[node] < dist:
            continue
        for next in graph[node]:
            cost = distance[node] + next[1]
            if cost < distance[next[0]]:
                distance[next[0]] = cost
                heapq.heappush(q, (cost, next[0]))

dijkstra(1)

oneToV = distance[V]
oneToP = distance[P]
dijkstra(P)
PToV = distance[V]

if oneToV == oneToP + PToV:
    print("SAVE HIM")
else:
    print("GOOD BYE")
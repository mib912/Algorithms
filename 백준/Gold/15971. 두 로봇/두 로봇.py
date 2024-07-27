import sys
sys.setrecursionlimit(10**7)

input = sys.stdin.readline

n, a, b = map(int, input().split())
ways = [[] for _ in range(n+1)]
visited = [[False]  for _ in range(n+1)]

for _ in range(n-1):
    x, y, cost = map(int, input().split())
    ways[x].append((y,cost))
    ways[y].append((x,cost))

def dfs(start, total, maxCost): # total: a가 b를 만날 떄까지의 비용, maxCost: 이동하면서 만난 최대비용
    visited[start] = True

    if start == b:
        print(total - maxCost)
        exit(0)
    
    for nxt, c in ways[start]:
        if visited[nxt] == True:
            continue
        dfs(nxt, total+c, max(maxCost, c))

if a == b:
    print(0)
else:
    dfs(a, 0, 0)
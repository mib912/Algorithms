import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n,m,k = map(int, input().split())
A = [0] + list(map(int, input().split()))

friends = [[] for _ in range(n+1)]

for _ in range(m):
    v,w = map(int, input().split())
    friends[v].append(w)
    friends[w].append(v)

visited = [False] * (n+1) # 친구 사이 Y/N
answer = 0

def dfs(x):
    visited[x] = True
    min_cost = A[x]
    for f in friends[x]:
        if not visited[f]:
            min_cost = min(min_cost, dfs(f))
    return min_cost


for i in range(1, n+1):
    if not visited[i]:
        answer += dfs(i)

if k >= answer:
    print(answer)
else:
    print("Oh no")
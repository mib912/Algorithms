import sys
sys.setrecursionlimit(10**7)

input = sys.stdin.readline

n, w = map(int, input().split())
tree = [[] for _ in range(n+1)]

for _ in range(n-1):
    u,v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

cnt = 0 # 리프노드 개수
for i in range(2, len(tree)): # 1은 루트노드
    if len(tree[i]) == 1: # 리프 노드라면
        cnt += 1
print("%.3f" %(w/cnt))
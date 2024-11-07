import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

n,m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)

s = int(input())
bearList = list(map(int, input().split()))

flag = False
def dfs(v):
    global flag
    if v in bearList: # 팬을 만난 경우
        return
    
    if graph[v] == []: # 시작노드에 간선이 없다면 투어는 끝
        flag = True
        return
        
    for i in graph[v]:
        if graph[i] != []: # i에 이어져있는 간선이 있을 때
            dfs(i)
        elif graph[i] == [] and i not in bearList: # leafnode 이고 팬을 만나지 않았다면
            flag = True

dfs(1)
if flag == False:
    print("Yes")
else:
    print("yes")

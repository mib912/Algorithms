
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

n = int(input())
nodes = list(map(int, input().split())) # 각 노드의 부모
rmv = int(input())

def dfs(del_node):
    nodes[del_node] = -99 # 노드제거
    for i in range(n):
        if del_node == nodes[i]: # del_node의 자식노드 제거
            dfs(i)

dfs(rmv)

cnt = 0 # 리프노드 개수
for i in range(n):
    if nodes[i] != -99 and i not in nodes: # 제거되지 않았고 부모노드리스트에 포함되지 않았다면
        cnt += 1

print(cnt)
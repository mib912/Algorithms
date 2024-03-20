import sys
from collections import deque
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

while True:
    n, k = map(int, input().split())
    if n == 0 and k == 0:
        break
    # depth 계산할 때 idx가 1일 때 루트노드랑 비교하기 때문에 나눠줌
    nodes = [-1] + list(map(int, input().split()))
    parent = [0] * (n+1)
    parent[0] = -1  # 첫번재 노드는 루트노드

    target_idx = 0
    depth = -1

    for i in range(1, n+1):
        if k == nodes[i]:
            target_idx = i  # 사촌 찾을 값의 idx
        if nodes[i] != nodes[i-1] + 1:  # 이전 노드 값과 비교하여 depth 계산
            depth += 1
        parent[i] = depth
    answer = 0
    # 부모는 다른데 부모의 부모가 같은 경우 cnt
    for i in range(1, n+1):
        if parent[i] != parent[target_idx] and parent[parent[i]] == parent[parent[target_idx]]:
            answer += 1
    print(answer)
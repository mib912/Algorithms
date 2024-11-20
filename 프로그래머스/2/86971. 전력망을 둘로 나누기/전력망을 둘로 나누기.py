from collections import deque

def bfs(v, n, trees):
    visited = [False for _ in range(n+1)]
    que = deque([v])
    visited[v] = True
    cnt = 1 # 이어져있는 전선의 송전탑 개수
        
    while que:
        now = que.popleft()
        for nxt in trees[now]:
            if visited[nxt] == False:
                visited[nxt] = True
                que.append(nxt)
                cnt += 1
    return cnt
    
def solution(n, wires):
    answer = n
    trees = [[] for _ in range(n+1)]
    
    for a,b in wires:
        trees[a].append(b)
        trees[b].append(a)
    
    for a,b in wires:
        # graph 선 자르기
        trees[a].remove(b)
        trees[b].remove(a)
        
        answer = min(abs(bfs(a,n,trees) - bfs(b,n,trees)), answer)
        
        # 다시 선 붙이기
        trees[a].append(b)
        trees[b].append(a)
    return answer
def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]
    
    def dfs(v):
        visited[v] = True
        for i in range(n): # v번이 누구와 연결되어있는지 확인
            if i != v and visited[i] == False: # 자기자신이 아니고
                if computers[v][i] == 1:
                    dfs(i)
        
    for com in range(n):
        if visited[com] == False:
            dfs(com)
            answer += 1
    
    return answer


        
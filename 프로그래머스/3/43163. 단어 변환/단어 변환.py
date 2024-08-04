from collections import deque
def solution(begin, target, words):
    answer = 0
    
    n = len(words)
    m = len(begin)
    
    visited = [False for _ in range(n)]
    depth = 0
    
    q = deque()
    q.append((begin, depth)) # word, depth
    
    while q:
        word, depth = q.popleft()
        if word == target:
            answer = depth
            break
        
        for i in range(n):
            tmp = 0 # 한글자가 다른 경우 찾기
            if visited[i] == False:
                for j in range(m):
                    if word[j] != words[i][j]:
                        tmp += 1
                if tmp == 1: # 한글자가 다른 경우
                    q.append((words[i], depth+1))
                    visited[i] = True
                        
    return answer
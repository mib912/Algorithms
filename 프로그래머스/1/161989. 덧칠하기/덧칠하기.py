def solution(n, m, section):
    answer = 0
    painted = 0 # 칠해진 마지막 벽
    
    for s in section:
        if s > painted: # 마지막으로 칠해진 벽 다음이라면
            painted = s + m -1 # 2에서 4칸 칠하면 2,3,4,5가 칠해짐
            answer += 1
    
    return answer
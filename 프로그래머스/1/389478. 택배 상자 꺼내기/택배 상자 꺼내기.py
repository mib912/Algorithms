def solution(n, w, num):
    answer = 0
    
    # num의 위치
    row = (num-1) // w
    pos = (num-1) % w
    
    # 실제 열
    if row % 2 == 0:
        col = pos
    else:
        col = w-1-pos
    
    # num과 같은 col에 위치한 수 세기
    last_row = (n-1)// w
    for i in range(row, last_row+1):
        if i % 2 == 0:
            box = i * w + (col + 1)
        else:
            box = i * w + (w - col)
            
        if box <= n:
            answer += 1
    
    return answer
def solution(n, times):
    answer = 0
    
    left = min(times)
    right = max(times) * n # 가장 오래걸릴 수 있는 경우
    
    while left <= right:
        mid = (left + right) // 2
        checked = 0
        
        for t in times:
            checked += mid // t # mid 시간 동안 t시간으로 심사 가능한 인원
        if checked >= n:
            right = mid - 1
            answer = mid
        else:
            left = mid + 1
    
    return answer
def solution(today, terms, privacies):
    answer = []
    d = {} # 약관 dict
    today = list(map(int, today.split('.')))
    # 일 단위로 변환
    today = today[0]*12*28 + today[1]*28 + today[2]
    
    for t in terms:
        n,m = t.split()
        d[n] = int(m) * 28 # 일 단위로 비교
    
    for idx, p in enumerate(privacies):
        date, info = p.split()
        date = list(map(int, date.split('.')))
        date = date[0]*12*28 + date[1]*28 + date[2]-1+d[info]
        
        if date < today:
            answer.append(idx+1)
        
    return answer
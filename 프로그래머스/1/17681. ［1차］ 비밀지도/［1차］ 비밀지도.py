def solution(n, arr1, arr2):
    answer = []
    
    for i in range(n):        
        num = bin(arr1[i] | arr2[i]) # bin() : 10진수 > 2진수 변환 2진수 변환후 or비트연산
        num = num[2:].zfill(n) # bin함수는 0b가 앞에 붙음
        # zfill함수로 n자리수만큼 앞에 0을 붙임
        num = num.replace('1','#').replace('0',' ')
        answer.append(num)
    print(answer)
    
    return answer


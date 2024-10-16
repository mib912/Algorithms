def solution(number, limit, power):
    nums = [] # 약수 list
    for i in range(1,number+1):
        cnt = 0
        for j in range(1,int(i**0.5)+1):
            if i % j == 0:
                cnt += 1
                if (j**2) != i: # 제곱근이 정수가 아닌경우 ex) 6의 약수 중 2,3
                    cnt += 1 # 2까지만 구해지므로 3을 구하기 위함
            if cnt > limit:
                cnt = power
                break # 이 이상 계산필요 X
        nums.append(cnt)
    return sum(nums)
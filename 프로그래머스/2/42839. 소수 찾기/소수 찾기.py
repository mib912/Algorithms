from itertools import permutations

def chkPrime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

def solution(numbers):
    nums = list(numbers)
    p_nums = []
    cnt = 0
    
    for i in range(1, len(numbers)+1):
        for p in permutations(nums, i):
            p_nums.append(int(''.join(p)))
    
    p_nums = list(set(p_nums))
    
    for i in p_nums:
        if chkPrime(i):
            cnt += 1
    return cnt
            
            
            
            
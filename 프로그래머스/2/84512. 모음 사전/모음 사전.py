from itertools import product
def solution(word):
    answer = 0
    vowels = ['A', 'E', 'I', 'O', 'U']
    dict = []
    for i in range(1,6):
        for v in product(vowels, repeat=i):
            dict.append(''.join(v))
    
    dict.sort()
    answer = dict.index(word)+1
    return answer
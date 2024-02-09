import sys
input = sys.stdin.readline

s = input()
q = int(input())

cnt = [[0 for _ in range(len(s)+1)] for _ in range(26)]

# 입력받은 문자열에 대한 누적합 초기화
for i in range(len(s)):
    for j in range(26):
        if ord(s[i]) - 97 == j: # ord(s[i]) - 97 > a~z를 0~25로 표현
            cnt[j][i+1] = cnt[j][i] + 1
        else: 
            cnt[j][i+1] = cnt[j][i]

for _ in range(q):
    alpha, l, r = input().split()
    answer = cnt[ord(alpha)-97][int(r)+1] - cnt[ord(alpha)-97][int(l)]
    print(answer)
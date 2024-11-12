import sys
input = sys.stdin.readline

n = int(input())
levels = []
answer = 0

for _ in range(n):
    levels.append(int(input()))

for i in range(n-1,0,-1): #뒤에서부터 난이도 조절
    if levels[i] <= levels[i-1]:
        answer += (levels[i-1] - levels[i] + 1) # 뒷난이도와 앞난이도 차이가 1이 나도록 수정 ex. 7, 5 > 7이 4가 되어야 한다. > 7-5+1
        levels[i-1] = levels[i] - 1

print(answer)
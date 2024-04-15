import sys

input = sys.stdin.readline

n = int(input())

pillar = []
for _ in range(n):
    w, h = map(int, input().split())
    pillar.append([w,h])

pillar.sort() # x축 기준으로 정렬

# 제일 높은 기둥의 인덱스 구하기
highest_idx = 0
for i in range(1,n):
    if pillar[highest_idx][1] < pillar[i][1]:
        highest_idx = i

# 왼쪽 > 최대높이 기둥
# 자신보다 높이가 큰 기둥을 만나면 높이 재설정
result = 0
x1, y1 = pillar[0]
for i in range(highest_idx+1):
    if pillar[i][1] >= y1:
        height = y1
        width = pillar[i][0] - x1
        result += height * width
        x1, y1 = pillar[i]

# 오른쪽 > 최대높이 기둥
a, b = pillar[-1]
for i in range(n-1, highest_idx-1, -1):
    if pillar[i][1] >= b:
        height = b
        width = a - pillar[i][0]
        result += height * width
        a, b = pillar[i]

result += pillar[highest_idx][1] # 가장 큰 기둥 너비
print(result)
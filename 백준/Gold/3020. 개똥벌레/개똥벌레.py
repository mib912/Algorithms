import sys
input = sys.stdin.readline

n, h = map(int, input().split())
top = [0] * (h+1)
bottom = [0] * (h+1)

# 종유석, 석순 나눠서 입력받기
for i in range(1, n+1):
    size = int(input())
    if i % 2 == 0:
        top[h-size+1] += 1
    else:
        bottom[size] += 1

# 석순 count -> h층부터 내려오면서 누적합
# 종유석 count -> 1층부터 올라오면서 누적합
for i in range(h, 0, -1):
    bottom[i-1] = bottom[i-1] + bottom[i]
    top[h-i+1] = top[h-i] + top[h-i+1]

for i in range(1, h+1):
    bottom[i] = bottom[i] + top[i]
bottom[0] = int(1e9)

print(min(bottom), bottom.count(min(bottom)))
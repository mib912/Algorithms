import sys
input = sys.stdin.readline

n = int(input())
cnt = 8 # 처음 daldidalgo 만들 때 쓰이는 횟수
i = 1
while True:
    if n - 2**i == 0:
        cnt = cnt + i + 2
        break
    elif n - 2**i < 0:
        cnt = cnt + i + 1
        break
    i += 1

print(cnt)
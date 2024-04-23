import sys
input = sys.stdin.readline

n = int(input())
cnt = 0

# n 개중 a에게 줄 짝수개 i를 빼고 c에게 줄 2개를 뺀 수에서 b,c가 나눠갖는다.
for i in range(2, n-1, 2): # 영훈이에게 줄 사탕 1개 빼기
    candy = n-i-2 # 남규에게 줄 사탕 최소 2개 빼기
    cnt += candy //2
print(cnt)
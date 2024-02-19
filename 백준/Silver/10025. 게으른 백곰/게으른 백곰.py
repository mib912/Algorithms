import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = [0]*1000001

last_idx = 0
for _ in range(n): # 마지막 인덱스 값 구해서 슬라이딩 윈도우 범위구하기
    g,x = map(int, input().split())
    arr[x] = g
    
    last_idx = max(last_idx, x) # 마지막 인덱스 값 구하기

window = 2*k + 1 # 좌우로 k만큼 닿고 양동이가 놓인 자리도 가능

ice = sum(arr[:window])
answer = ice
for i in range(window, last_idx+1):
    ice += arr[i] - arr[i-window]
    answer = max(answer, ice)

print(answer)
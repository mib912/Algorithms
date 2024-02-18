import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))
end = 0
cnt = 0  # 라이언인형 개수
answer = n
flag = False # 라이언인형 개수 k개이상 존재 확인

for start in range(n):
    while cnt < k and end < n:
        if arr[end] % 2 == 1:
            cnt += 1
        end += 1
    if cnt >= k:
        answer = min(answer, end-start)
        flag = True
    if arr[start] % 2 == 1:
        cnt -= 1
if flag == False:
    answer = -1
print(answer)
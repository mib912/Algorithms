import sys

input = sys.stdin.readline

n, s = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0

def recur(idx, subSum):
    global cnt
    if idx >= n:
        return
    
    subSum += arr[idx]
    if subSum == s:
        cnt += 1

    recur(idx+1, subSum) # 현재 arr[idx]를 선택하는 경우
    recur(idx+1, subSum-arr[idx]) # 현재 arr[idx]를 선택하지 않는 경우

recur(0,0)
print(cnt)
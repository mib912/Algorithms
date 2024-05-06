import sys

input = sys.stdin.readline

N,L,R,X = map(int, input().split())
levels = list(map(int, input().split()))

cnt = 0
ans = []
def recur(idx):
    global cnt
    if len(ans) > N:
        return
    if len(ans) >= 2:
        if L <= sum(ans) <= R and max(ans)-min(ans) >= X:
            cnt += 1

    for i in range(idx, N):
        ans.append(levels[i])
        recur(i+1)
        ans.pop() # 부모로 이동?

recur(0)
print(cnt)
import sys

input = sys.stdin.readline

n = int(input())
tastes = [list(map(int, input().split())) for _ in range(n)]
res = int(1e9)
taste = []


def recur(idx, taste, useCnt):
    global res
    S, B = 1, 0
    if useCnt >= 1:
        for s, b in taste:
            S *= s
            B += b
        res = min(res, abs(S-B))

    if idx >= n:
        return

    recur(idx+1, taste[:], useCnt)  # 사용하지 않은 경우
    taste.append(tastes[idx])
    recur(idx+1, taste[:], useCnt+1)  # 사용한 경우


recur(0, taste, 0)
print(res)
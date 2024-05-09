import sys

input = sys.stdin.readline

n = int(input())
colors = [list(map(int, input().split())) for _ in range(n)]
gRed, gGreen, gBlue = map(int, input().split())

mixColor = []
res = int(1e9)


def recur(idx, mixColor):
    global res

    mixCnt = len(mixColor)
    if mixCnt >= 2:
        R, G, B = 0, 0, 0  # 섞는 물감의 합계
        for r, g, b in mixColor:
            R += r
            G += g
            B += b

        R //= mixCnt
        G //= mixCnt
        B //= mixCnt
        res = min(res, abs(R - gRed) + abs(G - gGreen) + abs(B - gBlue))
    if idx >= n or mixCnt >= 7:  # n-1번째 물감을 검사 한 후 기저조건 비교해야 함
        return
    recur(idx+1, mixColor[:])  # 물감 사용하지 않는경우
    mixColor.append(colors[idx])
    recur(idx+1, mixColor[:])  # 물감 사용하는 경우


recur(0, mixColor)
print(res)
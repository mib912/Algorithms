import sys

input = sys.stdin.readline

A = []
for _ in range(3): # 이차원배열이 아닌 일차원배열로 입력 받기
    for a in list(map(int, input().split())):
        A.append(a)

magic = [0] * 9
visited = [False] * 10
cost = int(1e9)

def costCalc():
    tCost = 0
    for i in range(9):
        tCost += abs(A[i] - magic[i])
    return tCost


def check():
    tSum = 0
    for i in range(3): # 각 행 합 구하기
        tSum = 0
        for j in range(3):
            tSum += magic[i * 3 + j]
        if tSum != 15:
            return False
    
    for i in range(3): # 각 열 합 구하기
        tSum = 0
        for j in range(3):
            tSum += magic[i + 3 * j]
        if tSum != 15:
            return False
    # 대각선
    tSum = magic[0] + magic[4] + magic[8] 
    if tSum != 15:
        return False
    tSum = magic[2] + magic[4] + magic[6]
    if tSum != 15:
        return False
    return True

def recur(idx):
    global cost
    if idx == 9:
        if check():
            cost = min(costCalc(), cost)

    for i in range(1,10):
        if visited[i]:
            continue
        
        visited[i] = True
        magic[idx] = i
        recur(idx+1)
        visited[i] = False

recur(0)
print(cost)
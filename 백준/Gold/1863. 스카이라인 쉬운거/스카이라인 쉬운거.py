import sys
input = sys.stdin.readline

n = int(input())
buildings = [list(map(int, input().split())) for _ in range(n)]
buildings.sort() # x좌표 정렬

# 스택에 남는 건물이 없도록 마지막에 높이가 0 인 건물 추가
buildings.append([float('inf'), 0])

ans = 0
stack = [0] # 건물 높이를 저장하고 높이가 낮아질 때 pop 하여 건물 수를 셈

for x,y in buildings:
    while stack and y < stack[-1]: # 건물이 종료되는 시점
        stack.pop()
        ans += 1
    if y > stack[-1]: # 새로운 건물이 시작되는 시점
        stack.append(y)

print(ans)
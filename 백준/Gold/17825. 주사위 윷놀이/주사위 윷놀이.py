import sys
input = sys.stdin.readline

dice = list(map(int, input().split()))

graph = [[1],[2],[3],[4],[5],[6,21],[7],[8],[9],[10],[11,25],[12],[13],[14],[15],[16,27],[17],[18],[19],[20],[32],[22],
         [23],[24],[30],[26],[24],[28],[29],[24],[31],[20],[32]]

score = [0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,13,16,19,25,22,24,28,27,26,30,35,0]
answer = 0

def back(depth, result, horse):
    global answer
    if depth == 10:
        answer = max(answer, result)
        return
    
    for i in range(4):
        x = horse[i] # 현재 말 위치
        
        if len(graph[x]) == 2:
            x = graph[x][-1] # 파란길
        else:
            x = graph[x][0] # 빨간길
        
        for _ in range(1, dice[depth]): # 주사위 값 만큼 말 이동
            x = graph[x][0] # 위에서 한칸 이동했기 때문에 1칸 덜 이동
        
        if x == 32 or (x < 32 and x not in horse): # 목적지 도착 or 목적지 아니고 말이 없음
            before = horse[i] # 이전 말 위치
            horse[i] = x # 현재 말 위치

            back(depth+1, result + score[x], horse)
            horse[i] = before

back(0,0,[0,0,0,0])
print(answer)
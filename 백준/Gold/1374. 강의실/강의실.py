import sys
import heapq
input = sys.stdin.readline

n = int(input())
ls = []
for _ in range(n):
    c,s,e = map(int, input().split())
    ls.append([c,s,e])

ls.sort(key=lambda x : (x[1])) # 시작시간 정렬

room = []
heapq.heappush(room, ls[0][2]) # 가장 처음 시작하는 강의의 끝나는시간

for i in range(1,n):
    if ls[i][1] < room[0]: # 강의 시작하는 시간이 강의가 가장 빨리 끝나는 시간보다 빠르면
        heapq.heappush(room,ls[i][2]) # 강의 끝나는시간을 heapq에 넣어 강의실 + 1
    else: # 강의 시작하는 시간이 강의가 가장 빨리 끝나는 시간보다 느리면 > 그 강의실 이용
        heapq.heappop(room) # 가장 빨리 끝나는 강의실 out > 그 강의실 이용
        heapq.heappush(room, ls[i][2])
print(len(room))
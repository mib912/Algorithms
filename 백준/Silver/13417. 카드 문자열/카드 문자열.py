from collections import deque
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    cards = list(map(str, input().split()))
    que = deque(cards[0])
    word = cards[0]

    for i in range(1, n):
        if word >= cards[i]: # word가 더 뒷 순서
            que.appendleft(cards[i])
            word = cards[i] # 비교해줄 단어 , 제일 왼쪽에 위치
        else:
            que.append(cards[i])
    print(''.join(que))

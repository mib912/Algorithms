from collections import deque
import sys
input = sys.stdin.readline

n,k = map(int, input().split())

dist = [0] * 100001

q = deque()
q.append(n)

while q:
    cur = q.popleft()
    if cur == k:
        print(dist[cur])
        break

    for nxt in [cur+1, cur-1, cur*2]:
        if 0 <= nxt < 100001 and dist[nxt] == 0:
            dist[nxt] = dist[cur]+1
            q.append((nxt))
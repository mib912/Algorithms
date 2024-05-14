import sys
input = sys.stdin.readline

n = int(input())
schedule = [list(map(int, input().split())) for _ in range(n)]

res = 0

def recur(cur, p):
    global res
    if cur > n:
        return
    if cur == n:
        res = max(res, p)
        return
    
    recur(cur+1, p)
    recur(cur+schedule[cur][0], p+schedule[cur][1])

recur(0,0)
print(res)
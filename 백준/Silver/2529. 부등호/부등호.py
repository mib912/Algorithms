import sys
input = sys.stdin.readline

k = int(input())
arr = list(map(str, input().split()))

selected = []
visited = [False] * 10
def check(left, right, sign): # 왼쪽 숫자, 오른쪽 숫자, 부등호
    if sign == '<':
        return left < right
    else:
        return left > right
    
def recur(cur, num):
    if cur == k+1: # if k=2 정답이 되는 숫자는 3자리수
        selected.append(num)
        return
    for i in range(10):
        if visited[i]:
            continue
        if cur == 0 or check(num[-1], str(i), arr[cur-1]): # 첫번째 수 두번째 수 비교할 때 필요한 부등호는 arr[0]
            visited[i] = True
            recur(cur+1, num+str(i))
            visited[i] = False

recur(0,"")
print(max(selected))
print(min(selected))
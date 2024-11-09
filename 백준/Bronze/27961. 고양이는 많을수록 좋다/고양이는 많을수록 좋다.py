import sys
input = sys.stdin.readline

n = int(input())

answer = 0
cat = 1

if n == 0:
    print(0)
elif n == 1:
    print(1)
else:
    while cat != n:
        if cat >= n - cat: # 고양이 수가 n-cat보다 클경우 > 4마리 있는데 n이 6마리일 때
            cat += n - cat
            answer += 1
            
        else: # 고양이 수가 n-cat보다 작을경우
            cat += cat
            answer += 1
    print(answer+1)
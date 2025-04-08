import sys
#input = sys.stdin.readline

bars = input()
stack = []
answer = 0

for i in range(len(bars)):
    if bars[i] == '(':
        stack.append('(')
    else:
        stack.pop()
        if bars[i-1] == '(': # ) 직전 괄호가 (면 레이저
            answer += len(stack)
        else: # ) 직전 괄호가 )면 막대기의 끝
            answer += 1

print(answer)
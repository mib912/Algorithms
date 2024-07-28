import sys

input = sys.stdin.readline

s = input().rstrip()
stack = []
answer = 0

for c in s:
    if c == '(':
        stack.append(c)
    else: # )
        if stack: # 여는 괄호가 있다면
            stack.pop()
        else: 
            answer += 1

print(answer + len(stack)) # 짝이 맞지 않는 여는괄호의 남은 갯수
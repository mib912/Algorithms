import sys
input = sys.stdin.readline

result, score = 0,0
for _ in range(10):
    score = int(input())
    result += score
    if result == 100:
        break
    elif result > 100:
        if result - 100 <= 100 - (result - score):
            break
        else:
            result -= score
            break
print(result)
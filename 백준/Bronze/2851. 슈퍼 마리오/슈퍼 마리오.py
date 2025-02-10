import sys
input = sys.stdin.readline

mushrooms = []
for _ in range(10):
    mushrooms.append(int(input()))

total = 0
answer = []
for i in range(10):
    before = total
    total += mushrooms[i]

    if total > 100:
        if 100 - before > total - 100:
            answer.append(total)
        elif 100 - before < total - 100:
            answer.append(before)
        else:
            answer.append(total)
        break

    elif total == 100:
        answer.append(total)
        break
    elif i == 9 and total < 100:
        answer.append(total)
        break

print(max(answer))
import sys
input = sys.stdin.readline

# a^2 = b^2 + n
n = int(input())
answer = 0

for b in range(1, 501):
    for a in range(b, 501):
        if a**2 == b**2 + n:
            answer += 1

print(answer)
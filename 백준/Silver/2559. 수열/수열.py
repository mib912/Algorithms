import sys
input = sys.stdin.readline

n, k = map(int, input().split())
temps = list(map(int, input().split()))

tot = sum(temps[:k])
answer = tot
for i in range(k, n):
    tot += temps[i] - temps[i-k]
    answer = max(answer, tot)
print(answer)
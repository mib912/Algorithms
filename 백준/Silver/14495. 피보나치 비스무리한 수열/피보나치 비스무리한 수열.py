import sys
input = sys.stdin.readline

n = int(input())
fibo = {}
fibo[1] = 1
fibo[2] = 1
fibo[3] = 1

for i in range(4, n+1):
    fibo[i] = fibo[i-1] + fibo[i-3]

print(fibo[n])
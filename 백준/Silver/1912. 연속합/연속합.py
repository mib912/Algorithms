# 1912 연속합
import sys
input = sys.stdin.readline

n = int(input())
ls = list(map(int, input().split()))

for i in range(1, n):
    ls[i] = max(ls[i], ls[i-1]+ls[i])

print(max(ls))
import sys
input = sys.stdin.readline

n, k = map(int, input().split())

temps = list(map(int, input().split()))

partSum = sum(temps[:k])
result = [partSum]

for i in range(n-k): # n개의 수를  k씩 연속합을 구하면 나오는 갯수
    result.append(result[i]-temps[i]+temps[i+k])

print(max(result))
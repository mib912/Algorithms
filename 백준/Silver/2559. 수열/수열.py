import sys
input = sys.stdin.readline

n, k = map(int, input().split())
ls = list(map(int, input().split()))

partSum = sum(ls[:k])
result = [partSum]

for i in range(n-k):
    partSum = partSum + ls[i+k] - ls[i] 
    result.append(partSum)

print(max(result))
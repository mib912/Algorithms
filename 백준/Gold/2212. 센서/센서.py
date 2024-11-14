import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
ls = list(map(int, input().split()))

ls.sort()
dist = []
for i in range(n-1):
    dist.append(ls[i+1] - ls[i])


dist.sort()
print(sum(dist[:n-k]))
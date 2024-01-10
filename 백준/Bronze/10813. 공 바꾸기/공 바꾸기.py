n, m = map(int, input().split())
result = [i + 1 for i in range(n)]

for _ in range(m):
    i, j = map(int, input().split())
    tmp = result[i-1]
    result[i-1] = result[j-1]
    result[j-1] = tmp

for i in result:
    print(i, end=' ')

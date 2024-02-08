import sys
input = sys.stdin.readline

s = input()
q = int(input())

for _ in range(q):
    alpha, l, r = map(str, input().split())
    findT = s[int(l):int(r)+1]
    print(findT.count(alpha))
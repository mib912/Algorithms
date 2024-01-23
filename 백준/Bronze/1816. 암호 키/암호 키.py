import sys
input = sys.stdin.readline

nums = []

n = int(input())
for _ in range(n):
    nums.append(int(input()))

for i in range(n):
    for j in range(2, 1000001):
        if nums[i] % j == 0:
            print("NO")
            break
    if j == 1000000:
        print("YES")
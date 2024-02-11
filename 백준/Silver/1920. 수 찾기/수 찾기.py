import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
m = int(input())
nums = list(map(int, input().split()))

arr.sort()
for t in nums:
    flag = False
    target = t
    s = 0
    e = len(arr)-1
    while s <= e:
        m = (s + e) // 2
        if t == arr[m]:
            print(1)
            flag = True
            break
        elif t < arr[m]:
            e = m-1
        else:
            s = m+1
    if flag == False:
        print(0)
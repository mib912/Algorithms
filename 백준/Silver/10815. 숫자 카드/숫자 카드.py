import sys

read = sys.stdin.readline
        
n = int(input())
cards = list(map(int, read().split()))
m = int(input())
nums = list(map(int, read().split()))

cards.sort()
# binary_search
for num in nums:
  start = 0
  end = n-1
  exist = False
  while start <= end:
    mid = (start + end) // 2
    if num > cards[mid]:
      start = mid+1
    elif cards[mid] > num:
      end = mid-1
    else:
      exist = True
      break
  print(1 if exist else 0, end=' ')
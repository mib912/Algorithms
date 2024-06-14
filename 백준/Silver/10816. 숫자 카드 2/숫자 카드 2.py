import sys

read = sys.stdin.readline
        
n = int(input())
cards = list(map(int, read().split()))
m = int(input())
nums = list(map(int, read().split()))

count = {}
for card in cards:
  if card in count:
    count[card] += 1
  else:
    count[card] = 1

for num in nums:
  result = count.get(num)
  if result == None:
    print(0, end=' ')
  else:
    print(result, end=' ')
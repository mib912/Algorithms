import sys

read = sys.stdin.readline

n = int(read().rstrip())

nth = 666 # 비교할 숫자
cnt = 0

while True:
  if '666' in str(nth):
    cnt += 1

  if cnt == n:
    print(nth)
    break
  nth += 1
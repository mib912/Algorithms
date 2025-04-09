import sys
input = sys.stdin.readline

n = int(input())
pattern = input().split('*')
start = pattern[0]
end = pattern[1]

for _ in range(n):
    name = input()

    if len(name) >= (len(start)+len(end)) and name.startswith(start) and name.endswith(end):
        print("DA")
    else:
        print("NE")

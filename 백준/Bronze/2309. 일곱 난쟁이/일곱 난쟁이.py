from itertools import combinations
heights = []
for _ in range(9):
    heights.append(int(input()))

for h in list(combinations(heights, 7)):
    total = sum(h)
    if total == 100:
        for i in sorted(h):
            print(i)
        break
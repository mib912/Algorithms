import sys
input = sys.stdin.readline

heights = []
for _ in range(9):
    heights.append(int(input()))

heights.sort()
total = sum(heights)
for i in range(9):
    for j in range(i+1, 9):
        if total - heights[i] - heights[j] == 100:
            for h in heights:
                if h == heights[i] or h == heights[j]:
                    continue
                print(h)
            exit()
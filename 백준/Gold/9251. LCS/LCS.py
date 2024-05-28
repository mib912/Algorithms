import sys
input = sys.stdin.readline

str1 = input().rstrip()
str2 = input().rstrip()
lcs = [[0]*(len(str2)+1) for _ in range(len(str1)+1)]

for i in range(1, len(str1)+1):
    for j in range(1, len(str2)+1):
        if str1[i-1] == str2[j-1]:  # 두 문자열의 글자가 같은 경우
            lcs[i][j] = lcs[i-1][j-1] + 1
        else:
            lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])
print(lcs[-1][-1])
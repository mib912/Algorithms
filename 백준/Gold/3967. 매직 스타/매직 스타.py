import sys
input = sys.stdin.readline

board = [list(input().strip()) for _ in range(5)] # 매직스타를 위한 판
coords = [
    (0,4),
    (1,1), (1,3),(1,5),(1,7),
    (2,2),(2,6),
    (3,1),(3,3),(3,5),(3,7),
    (4,4)
] # 입력되는 알파벳 좌표

lines = [
    [0,2,5,7],
    [0,3,6,10],
    [1,2,3,4],
    [1,5,8,11],
    [4,6,9,11],
    [7,8,9,10]
] # 더해서 26이 되어야 하는 선의 values 인덱스 값 ex) values[0]+values[2]+values[5]+values[7]=26
values = [-1] * 12 # i좌표에 들어있는 값
used = [False] * 13

empty_idx = [] # x의 좌표의 인덱스

# 초기 상태 셋팅
for i, (r,c) in enumerate(coords):
    ch = board[r][c]
    if ch == 'x':
        empty_idx.append(i)
    else:
        num = ord(ch) - ord('A') + 1 # A:1, B:2 ~ L:12
        values[i] = num
        used[num] = True

def print_board():
    for i, (r,c) in enumerate(coords):
        board[r][c] = chr(values[i] + ord('A') - 1)
    for row in board:
        print(''.join(row))

def is_valid(): # 4개의 수의 합이 26이 되는지 확인
    for line in lines:
        nums = [values[i] for i in line]
        if -1 not in nums:
            if sum(nums) != 26:
                return False
    return True


def backtrack(idx):
    if idx == len(empty_idx):
        if is_valid():
            print_board()
            exit(0)
    
    pos = empty_idx[idx] # 'x'가 들어있는 좌표의 인덱스
    
    for num in range(1,13):
        if used[num]:
            continue # 이미 사용된 숫자
        values[pos] = num
        used[num] = True

        if is_valid():
            backtrack(idx+1)
        
        values[pos] = -1
        used[num] = False

backtrack(0)
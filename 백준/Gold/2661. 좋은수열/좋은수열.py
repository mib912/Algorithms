import sys
input = sys.stdin.readline

n = int(input())

def chkGood(seq):
    length = len(seq)
    for i in range(1, length//2+1):
        if seq[-i:] == seq[-2*i:-i]:
            return False
    return True


def dfs(seq, n):
    if len(seq) == n:
        print(seq)
        exit()

    for i in "123":
        new_seq = seq + i
        if chkGood(new_seq):
            dfs(new_seq, n)


dfs("", n)
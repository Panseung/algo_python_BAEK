# 11723. 집합
# Level Silver5
# Link : https://www.acmicpc.net/problem/11723


import sys


def solve(c, n):
    global S
    if c == 'add':
        S[n] = True
    elif c == 'remove':
        S[n] = False
    elif c == 'check':
        if S[n]:
            print(1)
        else:
            print(0)
    elif c == 'toggle':
        S[n] = not S[n]
    elif c == 'all':
        for i in range(1, 21):
            S[i] = True
    else:
        for i in range(1, 21):
            S[i] = False


S = [False] * 21
N = int(input())
for _ in range(N):
    tmp = list(sys.stdin.readline().split())
    cmd, num = 0, 0
    if len(tmp) == 2:
        cmd, num = tmp[0], int(tmp[1])
    else:
        cmd = tmp[0]
    solve(cmd, num)


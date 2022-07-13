# 5430. AC
# Level Gold5
# Link : https://www.acmicpc.net/problem/5430


import sys
from collections import deque

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    cmd = input().rstrip()
    n = int(input().rstrip())
    if n == 0:
        lst = []
        input()
    else:
        lst = deque(map(int, input().rstrip().strip(']').strip('[').split(',')))
    cmd_lst = []
    for i in range(len(cmd) - 1, -1, -1):
        cmd_lst.append(cmd[i])
    r_cnt = 0
    err = False
    while cmd_lst:
        c = cmd_lst.pop()
        if c == 'R':
            r_cnt += 1
        elif c == 'D':
            if lst:
                if r_cnt % 2:
                    lst.pop()
                else:
                    lst.popleft()
            else:
                print('error')
                err = True
                break
    if not err:
        if r_cnt % 2:
            lst.reverse()
        print('[', end='')
        result = ''
        for num in lst:
            result += str(num)
            result += ','
        result = result[0:-1]
        print(result, end='')
        print(']')

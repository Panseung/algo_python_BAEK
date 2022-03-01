# 1107. 리모컨
# Level Gold 5
# Link : https://www.acmicpc.net/problem/1107

import sys

my_input = sys.stdin.readline


def solve(v, k):
    if k == length:
        lst.append(v)
        return
    else:
        for i in range(10):
            pluns_num = int(v[k]) + i
            minus_num = int(v[k]) - i
            stop = False
            if pluns_num < 10 and pluns_num not in broken_btn:
                solve(pluns_num * 10 ** (length - 1 - k), k + 1)
                stop = True
            if minus_num >= 0 and minus_num not in broken_btn:
                solve((minus_num + 1) * 10 ** (length - 1 - k) - 1, k + 1)
                stop = True
            if stop:
                break


N = my_input().rstrip()
M = int(my_input())
broken_btn = list()
move_100 = abs(100 - int(N))
length = len(N)
if M:
    broken_btn = list(map(int, my_input().split()))
    lst = list()
    solve(N, 0)
    print(lst)
else:
    print(min(move_100, length))

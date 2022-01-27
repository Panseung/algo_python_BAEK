# 4153. 직각삼각형
# Level Bronze3
# Link : https://www.acmicpc.net/problem/4153

import sys

while True:
    lst = list(map(int, sys.stdin.readline().split()))
    if sum(lst) == 0:
        break
    lst.sort()
    if lst[0] ** 2 + lst[1] ** 2 == lst[2] ** 2:
        print('right')
    else:
        print('wrong')


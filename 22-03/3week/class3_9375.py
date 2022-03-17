# 9375. 패션왕
# Level Silver3
# Link : https://www.acmicpc.net/problem/9375

import sys

my_input = sys.stdin.readline

T = int(my_input())
for tc in range(T):
    n = int(my_input())
    lst = list()
    for _ in range(n):
        a, b = my_input().split()
        lst.append(b)

    set_lst = list(set(lst))
    result = 1
    for a in set_lst:
        tmp = 1
        for b in lst:
            if a == b:
                tmp += 1
        result *= tmp
    print(result - 1)

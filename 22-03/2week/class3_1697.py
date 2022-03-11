# 1697. 숨바꼭질
# Level Silver1
# Link : https://www.acmicpc.net/problem/1697

import sys
from collections import deque


def solve():
    q = deque()
    q.append(N)
    while q:
        res = q.popleft()
        if res == K:
            print(lst[res])
            break

        for nex in (res - 1, res + 1, 2 * res):
            if 0 <= nex <= 100000 and not lst[nex]:
                lst[nex] = lst[res] + 1
                q.append(nex)


my_input = sys.stdin.readline

N, K = map(int, my_input().split())

lst = [0] * 100001
solve()

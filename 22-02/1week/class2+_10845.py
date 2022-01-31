# 10845. 큐
# Level Silver4
# Link : https://www.acmicpc.net/problem/10845

import sys
from collections import deque

my_input = sys.stdin.readline


def my_func(func):
    if func == 'front':
        if Q:
            return print(Q[0])
        else:
            return print(-1)
    elif func == 'pop':
        if Q:
            return print(Q.popleft())
        else:
            return print(-1)
    elif func == 'size':
        return print(len(Q))
    elif func == 'empty':
        if Q:
            return print(0)
        else:
            return print(1)
    elif func == 'back':
        if Q:
            return print(Q[-1])
        else:
            return print(-1)


Q = deque()
N = int(my_input())
for _ in range(N):
    func = my_input().strip()
    if len(func) >= 6:
        Q.append(func[5:])
    else:
        my_func(func)

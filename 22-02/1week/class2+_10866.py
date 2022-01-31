# 10866. 덱
# Level Silver4
# Link : https://www.acmicpc.net/problem/10866

import sys
from collections import deque

my_input = sys.stdin.readline


def my_func(func):
    if func == 'pop_front':
        if Q:
            return print(Q.popleft())
        else:
            return print(-1)
    elif func == 'pop_back':
        if Q:
            return print(Q.pop())
        else:
            return print(-1)
    elif func == 'size':
        return print(len(Q))
    elif func == 'empty':
        if Q:
            return print(0)
        else:
            return print(1)
    elif func == 'front':
        if Q:
            return print(Q[0])
        else:
            return print(-1)
    elif func == 'back':
        if Q:
            return print(Q[-1])
        else:
            return print(-1)


Q = deque()
N = int(my_input())
for _ in range(N):
    func = my_input().strip()
    if len(func) >= 11:
        if func[5] == 'b':
            Q.append(func[10:])
        elif func[5] == 'f':
            Q.appendleft(func[11:])
    else:
        my_func(func)

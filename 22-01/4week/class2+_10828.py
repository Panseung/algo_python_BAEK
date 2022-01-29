# 10828. 스택
# Level Silver4
# Link : https://www.acmicpc.net/problem/10828

import sys

my_input = sys.stdin.readline()


def my_func(func):
    if func == 'top':
        if stack:
            return print(stack[-1])
        else:
            return print(-1)
    elif func == 'pop':
        if stack:
            return print(stack.pop())
        else:
            return print(-1)
    elif func == 'size':
        return print(len(stack))
    elif func == 'empty':
        if stack:
            return print(0)
        else:
            return print(1)


stack = list()
N = int(my_input())
for _ in range(N):
    func = my_input()
    if len(func) >= 6:
        stack.append(func[5:])
    else:
        my_func(func)

# 1003. 피보나치 함수
# Level Silver 3
# Link : https://www.acmicpc.net/problem/1003

import sys


def fibonacci(num):
    if num == 0:
        result[0] += 1
    elif num == 1:
        result[1] += 1
    else:
        fibonacci(num - 1)
        fibonacci(num - 2)


my_input = sys.stdin.readline

T = int(my_input())
for tc in range(T):
    N = int(my_input())
    result = [0, 0]
    fibonacci(N)
    print(*result)
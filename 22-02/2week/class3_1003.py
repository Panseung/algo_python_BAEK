# 1003. 피보나치 함수
# Level Silver 3
# Link : https://www.acmicpc.net/problem/1003

import sys

zero = [1, 0, 1]
one = [0, 1, 1]


def fibonacci(num):
    length = len(zero)
    if num >= length:
        for i in range(length, num + 1):
            zero.append(zero[i - 1] + zero[i - 2])
            one.append(one[i - 1] + one[i - 2])
    print(zero[num], one[num])


my_input = sys.stdin.readline

T = int(my_input())
for tc in range(T):
    N = int(my_input())
    fibonacci(N)

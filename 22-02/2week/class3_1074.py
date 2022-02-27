# 9095. Z
# Level Silver 1
# Link : https://www.acmicpc.net/problem/1074

import sys

my_input = sys.stdin.readline

N, r, c = map(int, my_input().split())

result = 0
while N != 0:
    N -= 1
    comV = 2 ** N
    if r >= comV:
        if c >= comV:
            result += comV ** 2 * 3
            c -= comV
        else:
            result += comV ** 2 * 2
        r -= comV
    else:
        if c >= comV:
            result += comV ** 2
            c -= comV

print(result)
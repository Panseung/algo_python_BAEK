# 2751. 수 정렬하기 2
# Level Silver5
# Link : https://www.acmicpc.net/problem/2751

import sys

T = int(input())
for tc in range(T):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())

    apart = [[0] * n for _ in range(k + 1)]
    for y in range(k + 1):
        for x in range(n):
            if y == 0:
                apart[y][x] = x + 1
            else:
                if x == 0:
                    apart[y][x] = 1
                else:
                    apart[y][x] = apart[y][x - 1] + apart[y - 1][x]
    print(apart[k][n - 1])

# 11651. 좌표 정렬하기 2
# Level Silver5
# Link : https://www.acmicpc.net/problem/11651

import sys

my_input = sys.stdin.readline

N = int(my_input())

lst = list()
for _ in range(N):
    lst.append(list(map(int, my_input().split())))
lst.sort()
lst.sort(key=lambda x: x[1])
for result in lst:
    print(*result)

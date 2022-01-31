# 11650. 좌표 정렬하기
# Level Silver5
# Link : https://www.acmicpc.net/problem/11650

import sys

my_input = sys.stdin.readline

N = int(my_input())
lst = list()
for _ in range(N):
    lst.append(list(map(int, my_input().split())))
lst.sort()
for x, y in lst:
    print(x, y)

# 10989. 수 정렬하기3
# Level Silver5
# Link : https://www.acmicpc.net/problem/10989

import sys

my_input = sys.stdin.readline

N = int(my_input())
lst = [0] * 10001
for _ in range(N):
    lst[int(my_input())] += 1

for i in range(10001):
    if lst[i]:
        for j in range(lst[i]):
            print(i, sep='\n')

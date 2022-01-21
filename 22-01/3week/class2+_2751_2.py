# 2751. 수 정렬하기 2
# Level Silver5
# Link : https://www.acmicpc.net/problem/2751

import sys

N = int(input())
num_lst = list()
for _ in range(N):
    num_lst.append(int(sys.stdin.readline()))

min_num = min(num_lst)
max_num = max(num_lst)

lst = [0] * (max_num )

# 11659. 구간 합 구하기 4
# Level Silver3
# Link : https://www.acmicpc.net/problem/11659


import sys

N, M = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
for _ in range(N):
    s, e = map(int, sys.stdin.readline().split())
    s -= 1
    result = 0
    sum_lst = [0]
    for i in range(1, N + 1):
        sum_lst.append(sum_lst[i - 1] + nums[i - 1])

    print(sum_lst[e] - sum_lst[s])

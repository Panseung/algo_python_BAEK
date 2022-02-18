# 1546. 평균
# Level Bronze1
# Link : https://www.acmicpc.net/problem/1546

import sys

my_input = sys.stdin.readline

N = int(my_input())
lst = list(map(int, my_input().split()))

my_mean = max(lst)
result = list()
for score in lst:
    result.append(score / my_mean * 100)

mean = sum(result) / len(result)

print(mean)

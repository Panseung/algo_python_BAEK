# 2805. 나무 자르기
# Level Silver3
# Link : https://www.acmicpc.net/problem/2805


import sys
from collections import Counter

num, target = map(int, sys.stdin.readline().split())

ary = list(map(int, sys.stdin.readline().split()))  # 개수는 num
counter = Counter(ary)
result = max(ary) + 1
cnt = 0


def midsum(mid):
    sum = 0
    for k, v in counter.items():
        if k > mid:
            sum += (k - mid) * v  # v는 갯수
    return sum

l = 0
r = 1000000000

while l <= r:
    m = (l + r) // 2
    cnt = midsum(m)

    if cnt < target:
        r = m - 1
    else:
        l = m + 1
        result = m

print(result)

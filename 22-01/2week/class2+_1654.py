# 1654. 랜선 자르기
# Level Silver3
# Link : https://www.acmicpc.net/problem/1654

import math

K, N = map(int, input().split())
lines = list()
for k in range(K):
    lines.append(int(input()))

start, end = 1, max(lines)

while start <= end:
    mid = (start + end) // 2
    line_cnt = 0
    for line in lines:
        line_cnt += line // mid

    if line_cnt >= N:
        start = mid + 1
    else:
        end = mid - 1

print(end)

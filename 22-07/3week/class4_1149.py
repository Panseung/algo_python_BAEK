# 1149. RGB거리
# Level Silver1
# Link : https://www.acmicpc.net/problem/1149

import sys

N = int(sys.stdin.readline())
houses = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
answer = 1e9
dp = [1e9] * N
color = 0

for i in range(3):
    val1 = houses[0][i]
    for j in range(3):
        if i == j:
            continue
        for k in range(3):
            val2 = val1 + houses[1][j]
            if j == k:
                continue
            val3 = val2 + houses[2][k]
            if val3 < dp[1]:
                dp[2] = val3
                dp[1] = val2
                dp[0] = val1
                color = j

idx = 3
while idx < N:
    res_v = dp[idx - 2]
    next_color = color
    for i in range(3):
        if i == color:
            continue
        for j in range(3):
            if i == j:
                continue
            next_v = res_v + houses[idx - 1][i] + houses[idx][j]
            if dp[idx] > next_v:
                dp[idx - 1] = res_v + houses[idx - 1][i]
                dp[idx] = next_v
                next_color = i
    idx += 1
    color = next_color
print(dp[N - 1])

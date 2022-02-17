# 1463. 1로 만들기
# Level Silver3
# Link : https://www.acmicpc.net/problem/1463

import sys

my_input = sys.stdin.readline

N = int(my_input())

dp = [0] * (N + 1)
for i in range(2, N + 1):
    dp[i] = dp[i - 1] + 1
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)
print(dp[N])

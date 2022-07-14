# 17626. Four Squares
# Level Silver3
# Link : https://www.acmicpc.net/problem/17626

import sys

n = int(sys.stdin.readline())
dp = [0, 1]
for i in range(2, n + 1):
    j = 1
    min_v = 3
    while j ** 2 <= i:
        min_v = min(min_v, dp[i - j ** 2])
        j += 1
    dp.append(min_v + 1)

print(dp[n])

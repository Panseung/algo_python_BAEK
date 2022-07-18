# 16928. 뱀과 사다리 게임
# Level Gold5
# Link : https://www.acmicpc.net/problem/16928

import sys


def ladder(pos):
    if pos >= 100:
        return
    for i in range(6, 0, -1):
        np = min(100, pos + i)
        if np == brd[np]:
            if dp[pos] + 1 < dp[np]:  # 사다리 or 뱀 없을 때
                dp[np] = dp[pos] + 1
                ladder(np)
        else:  # 사다리 or 뱀 있을 때
            if dp[pos] + 1 < dp[brd[np]]:
                dp[brd[np]] = dp[pos] + 1
                ladder(brd[np])


N, M = map(int, sys.stdin.readline().split())

brd = [i for i in range(101)]

for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())
    brd[a] = b

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    brd[a] = b

dp = [99] * 101
dp[0] = 0
dp[1] = 0
ladder(1)
# for i in range(1, 101, 10):
#     print(dp[i: i + 10])
print(dp[100])

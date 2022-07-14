# 16928. 뱀과 사다리 게임
# Level Gold5
# Link : https://www.acmicpc.net/problem/16928

import sys

N, M = map(int, sys.stdin.readline().split())

brd = [i for i in range(101)]

for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())
    brd[a] = b

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    brd[a] = b

dp = [99] * 101
for i in range(1, 7):
    dp[i] = 1

changed = False
min_num = 100
lst = []
for i in range(1, 101):
    for j in range(1, 7):
        dp[min(i + j, 100)] = min(dp[min(i + j, 100)], dp[i] + 1)
    if i != brd[i]:
        min_v = min(dp[brd[i]], dp[i])
        if i > brd[i] and dp[brd[i]] != min_v:
            print(i, dp[brd[i]], min_v)
            changed = True
            lst.append(i)
            if i < min_num:
                min_num = i
        dp[brd[i]] = min_v
print(brd)
while changed:
    changed = False
    print(lst)
    lst = []
    for i in range(min_num, 101):
        for j in range(1, 7):
            dp[min(i + j, 100)] = min(dp[min(i + j, 100)], dp[i] + 1)
        if i != brd[i]:
            min_v = min(dp[brd[i]], dp[i])
            if i > brd[i] and dp[brd[i]] != min_v:
                changed = True
                if i < min_num:
                    min_num = i
            dp[brd[i]] = min_v

for i in range(1, 101, 10):
    print(dp[i:i+10])
print(dp[100])

# 1043. 거짓말
# Level Gold4
# Link : https://www.acmicpc.net/problem/1043

import sys

N, M = map(int, sys.stdin.readline().split())

lst = list(map(int, sys.stdin.readline().split()))


party = []
for _ in range(M):
    party.append(list(map(int, sys.stdin.readline().split())))



for i in range(1, lst[0] + 1):
    for j in range(M):
        if lst[i] in party[j]:
            M -= 1
            break

print(M)

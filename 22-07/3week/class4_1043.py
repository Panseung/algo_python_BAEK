# 1043. 거짓말
# Level Gold4
# Link : https://www.acmicpc.net/problem/1043

import sys

N, M = map(int, sys.stdin.readline().split())

lst = list(map(int, sys.stdin.readline().split()))

people = [False] * (N + 1)

for i in range(1, lst[0] + 1):
    people[lst[i]] = True

parties = list()

for _ in range(M):
    parties.append(list(map(int, sys.stdin.readline().split())))

chaged = True
while chaged:
    chaged = False
    for party in parties:
        for i in range(1, party[0] + 1):
            if people[party[i]]:
                for j in range(1, party[0] + 1):
                    if not people[party[j]]:
                        people[party[j]] = True
                        chaged = True
                break

for party in parties:
    for i in range(1, party[0] + 1):
        if people[party[i]]:
            M -= 1
            break

print(M)

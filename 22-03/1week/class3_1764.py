# 1764. 듣보잡
# Level Silver4
# Link : https://www.acmicpc.net/problem/1764

import sys

my_input = sys.stdin.readline

N, M = map(int, my_input().split())
lst = list()
for _ in range(N + M):
    lst.append(my_input().rstrip())
lst.sort()
result = list()

for i in range(N + M - 1):
    if lst[i] == lst[i + 1]:
        result.append(lst[i])

print(len(result))

for res in result:
    print(res)

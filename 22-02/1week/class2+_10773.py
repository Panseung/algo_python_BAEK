# 10989. 수 정렬하기3
# Level Silver5
# Link : https://www.acmicpc.net/problem/10989

import sys

my_input = sys.stdin.readline

K = int(my_input().rstrip())
ledger = list()
for _ in range(K):
    num = int(my_input().rstrip())
    if num > 0:
        ledger.append(num)
    else:
        ledger.pop()

print(sum(ledger))

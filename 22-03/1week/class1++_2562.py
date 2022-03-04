# 2562. 최댓값
# Level Bronze2
# Link : https://www.acmicpc.net/problem/2562

import sys

my_input = sys.stdin.readline

lst = list()
for _ in range(9):
    lst.append(int(my_input()))

maxV = max(lst)
maxIdx = lst.index(maxV)

print(maxV)
print(maxIdx + 1)

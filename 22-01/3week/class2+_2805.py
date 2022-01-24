# 2805. 나무 자르기
# Level Silver3
# Link : https://www.acmicpc.net/problem/2805

import sys

N, M = map(int, input().split())
trees = list(map(int, sys.stdin.readline().split()))

start = 0
end = max(trees)

while start < end:
    middle = (start + end) // 2
    cnt = 0
    for tree in trees:
        if tree > middle:
            cnt += tree - middle
    if cnt > M:
        start = middle
    elif cnt == M:
        start = middle
        break
    else:
        end = middle
print(start)

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

    if end - start == 1:
        cnt = 0
        for tree in trees:
            if tree > end:
                cnt += tree - end
        if cnt >= M:
            start = end
        break
    elif cnt >= M:
        start = middle
    else:
        end = middle - 1
print(start)

# 2805. 나무 자르기
# Level Silver3
# Link : https://www.acmicpc.net/problem/2805

import sys

N, M = map(int, input().split())
tree = list(map(int, sys.stdin.readline().split()))

max_height = max(tree)
for height in range(max_height, -1, -1):
    sumV = 0
    for i in range(N):
        if tree[i] > height:
            sumV += tree[i] - height
    if sumV >= M:
        print(height)
        break

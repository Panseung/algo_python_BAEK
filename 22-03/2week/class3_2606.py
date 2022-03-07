# 2606. 바이러스
# Level Silver3
# Link : https://www.acmicpc.net/problem/2606

import sys
from collections import deque

my_input = sys.stdin.readline

N = int(my_input())
cnt = int(my_input())

lst = [[] for _ in range(N + 1)]
for _ in range(cnt):
    a, b = map(int, my_input().split())
    lst[a].append(b)
    lst[b].append(a)

Q = deque()
Q.append(1)
visited = [0] * (N + 1)
visited[1] = 1
result = 0

while Q:
    num = Q.popleft()
    for i in lst[num]:
        if not visited[i]:
            visited[i] = 1
            Q.append(i)
            result += 1

print(result)
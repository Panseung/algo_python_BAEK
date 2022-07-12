# 1927. 최소 힙
# Level Silver2
# Link : https://www.acmicpc.net/problem/1927

import sys
from collections import deque

N = int(input())
q = deque()

for _ in range(N):
    cmd = int(sys.stdin.readline().rstrip())
    if cmd > 0:
        q.append(cmd)
    else:
        if q:
            q = deque(sorted(q))
            print(q.popleft())
        else:
            print(0)

# 11279. 최대 힙
# Level Silver2
# Link : https://www.acmicpc.net/problem/11279

import sys
import heapq

N = int(input())
heap = []

for _ in range(N):
    cmd = int(sys.stdin.readline().rstrip())
    if cmd > 0:
        heapq.heappush(heap, -cmd)
    else:
        if heap:
            print(-heapq.heappop(heap))
        else:
            print(0)


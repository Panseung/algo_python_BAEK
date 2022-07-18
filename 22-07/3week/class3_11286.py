# 11286. 절댓값 힙
# Level Silver1
# Link : https://www.acmicpc.net/problem/11286

import sys
import heapq

N = int(input())
heap = []

for _ in range(N):
    cmd = int(sys.stdin.readline().rstrip())
    if cmd:
        heapq.heappush(heap, [abs(cmd), cmd])
    else:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)


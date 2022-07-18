# 7662. 이중 우선순위 큐
# Level Gold4
# Link : https://www.acmicpc.net/problem/7662

import sys
import heapq

T = int(sys.stdin.readline())
for _ in range(T):
    k = int(sys.stdin.readline())
    min_heap = list()
    max_heap = list()
    length = 0
    visited = [False] * 1000001
    for i in range(k):
        c, n = sys.stdin.readline().split()
        n = int(n)
        if c == 'I':
            length += 1
            heapq.heappush(min_heap, [n, i])
            heapq.heappush(max_heap, [-n, i])
            visited[i] = True

        elif length:
            length -= 1
            if length == 0:
                max_heap, min_heap = [], []
            else:
                if n > 0:
                    while max_heap and not visited[max_heap[0][1]]:
                        heapq.heappop(max_heap)
                    if max_heap:
                        visited[max_heap[0][1]] = False
                        heapq.heappop(max_heap)
                else:
                    while min_heap and not visited[min_heap[0][1]]:
                        heapq.heappop(min_heap)
                    if min_heap:
                        visited[min_heap[0][1]] = False
                        heapq.heappop(min_heap)

    while max_heap and not visited[max_heap[0][1]]:
        heapq.heappop(max_heap)
    while min_heap and not visited[min_heap[0][1]]:
        heapq.heappop(min_heap)

    if length:
        print(-max_heap[0][0], min_heap[0][0])
    else:
        print('EMPTY')

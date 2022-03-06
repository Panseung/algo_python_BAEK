# 1389. 케빈 베이컨 6단계
# Level Silver1
# Link : https://www.acmicpc.net/problem/1389

import sys
from collections import deque

my_input = sys.stdin.readline

N, M = map(int, my_input().split())
lst = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, my_input().split())
    lst[a].append(b)
    lst[b].append(a)

result = N ** 2
result_num = 0
for i in range(1, N + 1):
    res_result = 0
    visited = [0] * (N + 1)
    visited[i] = 1
    Q = deque()
    Q.append([i, 1])
    while sum(visited) < N:
        num, turn = Q.popleft()
        for j in lst[num]:
            if not visited[j]:
                visited[j] = 1
                Q.append([j, turn + 1])
                res_result += turn

    if result > res_result:
        result = res_result
        result_num = i
    elif result == res_result:
        result_num = min(result_num, i)

print(result_num)

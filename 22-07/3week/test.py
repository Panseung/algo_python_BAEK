# 1167. 트리의 지름
# Level Gold2
# Link : https://www.acmicpc.net/problem/1167

import sys

inf = int(1e9)

V = int(input())

graph = [[inf] * (V + 1) for _ in range(V + 1)]

for a in range(1, V + 1):
    for b in range(1, V + 1):
        if a == b:
            graph[a][b] = 0

for _ in range(1, V + 1):
    lst = list(map(int, sys.stdin.readline().split()))
    i = lst[0]
    for j in range(1, len(lst) - 1, 2):
        a, b = lst[j], lst[j + 1]
        graph[i][a] = b

answer = 0

for k in range(1, V + 1):
    for a in range(1, V + 1):
        for b in range(1, V + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
            if graph[a][b] != inf and graph[a][b] > answer:
                answer = graph[a][b]
print(answer)

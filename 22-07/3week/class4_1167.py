# 1167. 트리의 지름
# Level Gold2
# Link : https://www.acmicpc.net/problem/1167

import sys

V = int(sys.stdin.readline())
graph = [[] for _ in range(V)]

for _ in range(V):
    lst = list(map(int, sys.stdin.readline().split()))
    i = lst[0] - 1
    for j in range(1, len(lst) - 1, 2):
        a, b = lst[j], lst[j + 1]
        graph[i].append([a - 1, b])

visited = [False] * V
visited[0] = True
answer = 0
cnt = 1
idx = 0
while cnt < V:
    distance = 0
    visit_idx = -1
    for i, d in graph[idx]:
        if distance < d and not visited[i]:
            distance = d
            visit_idx = i
    visited[visit_idx] = True
    if visit_idx == -1:
        break
    idx = visit_idx
    cnt += 1
    answer += distance
    print(idx)

print('here', idx)
visited = [False] * V
visited[idx] = True
answer = 0
cnt = 1
while cnt < V:
    distance = 0
    visit_idx = -1
    for i, d in graph[idx]:
        if distance < d and not visited[i]:
            distance = d
            visit_idx = i
    visited[visit_idx] = True
    idx = visit_idx
    cnt += 1
    answer += distance
    print(idx)

print(answer)

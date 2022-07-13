# 11403. 경로 찾기
# Level Silver1
# Link : https://www.acmicpc.net/problem/11403

from collections import deque

N = int(input())
graph = [[] for _ in range(N)]

brd = [list(map(int, input().split())) for _ in range(N)]
for y in range(N):
    for x in range(N):
        if brd[y][x] == 1:
            graph[y].append(x)

answer_graph = [[0] * N for _ in range(N)]

for i in range(N):
    goals = []
    visited = [0] * N
    q = deque()
    for v in graph[i]:
        q.append(v)
        goals.append(v)
    while q:
        v = q.popleft()
        for v2 in graph[v]:
            if not visited[v2]:
                visited[v2] = 1
                q.append(v2)
                goals.append(v2)
    goals = set(goals)
    for g in goals:
        answer_graph[i][g] = 1

for a in answer_graph:
    print(*a)

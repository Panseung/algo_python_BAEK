# 1107. DFS와 BFS
# Level Silver 2
# Link : https://www.acmicpc.net/problem/1260

import sys
from collections import deque

my_input = sys.stdin.readline


def dfs(v):
    dfs_result.append(v)
    for num in lines[v]:
        if not dfs_visited[num]:
            dfs_visited[num] = 1
            dfs(num)
            break


def bfs(v):
    Q = deque()
    Q.append(v)
    while len(bfs_result) < N and Q:
        start = Q.popleft()
        if not bfs_visited[start]:
            bfs_visited[start] = 1
            bfs_result.append(start)
            for num in lines[start]:
                Q.append(num)



N, M, V = map(int, my_input().split())
lines = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, my_input().split())
    lines[a].append(b)
    lines[b].append(a)

for i in range(1, N + 1):
    lines[i].sort()

dfs_visited = [0] * (N + 1)
dfs_visited[V] = 1
dfs_result = []
dfs(V)

bfs_visited = [0] * (N + 1)
bfs_result = []
bfs(V)
print(*dfs_result)
print(*bfs_result)

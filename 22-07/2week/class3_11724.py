# 11724. 연결 요소의 개수
# Level Silver2
# Link : https://www.acmicpc.net/problem/11724


import sys

N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (N + 1)
answer = 0
for i in range(1, N + 1):
    if not visited[i]:
        stack = []
        visited[i] = True
        stack.append(i)
        answer += 1
        while stack:
            v = stack.pop()
            for j in graph[v]:
                if not visited[j]:
                    visited[j] = True
                    stack.append(j)
print(answer)
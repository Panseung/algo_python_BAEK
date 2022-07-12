# 1260. DFS와 BFS
# Level Silver2
# Link : https://www.acmicpc.net/problem/1260


from collections import deque

def dfs(num):
    for j in graph[num]:
        if not visited[j]:
            visited[j] = True
            result_dfs.append(j)
            dfs(j)


n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for line in graph:
    line.sort()

result_dfs = []

visited = [False] * (n + 1)
visited[v] = True
result_dfs.append(v)
dfs(v)

print(*result_dfs)

result_bfs = []
visited = [False] * (n + 1)
visited[v] = True
result_bfs.append(v)
q = deque()
q.append(v)
while q:
    v = q.popleft()
    for i in graph[v]:
        if not visited[i]:
            q.append(i)
            visited[i] = True
            result_bfs.append(i)
print(*result_bfs)
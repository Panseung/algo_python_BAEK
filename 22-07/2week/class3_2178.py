# 2178. 미로 탐색
# Level Silver1
# Link : https://www.acmicpc.net/problem/2178


from collections import deque
import sys

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

N, M = map(int, sys.stdin.readline().split())
maze = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
q = deque()
q.append([0, 0, 1])
while q:
    y, x, cnt = q.popleft()
    find = False
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < N and 0 <= nx < M and maze[ny][nx] == '1' and not visited[ny][nx]:
            if ny == N - 1 and nx == M - 1:
                find = True
                print(cnt + 1)
                break
            visited[ny][nx] = 1
            q.append([ny, nx, cnt + 1])
    if find:
        break

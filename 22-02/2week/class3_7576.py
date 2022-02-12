# 7576. 토마토
# Level Gold5
# Link : https://www.acmicpc.net/problem/7576

from collections import deque
import sys
my_input = sys.stdin.readline

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

M, N = map(int, my_input().split())  # 가로, 세로
box = []
for _ in range(N):
    box.append(list(map(int, my_input().split())))

max_cnt = M * N
for y in range(N):
    for x in range(M):
        if box[y][x] == -1:
            max_cnt -= 1

visited = [[0] * M for _ in range(N)]
Q = deque()
cnt = 0

for y in range(N):
    for x in range(M):
        if box[y][x] == 1:
            Q.append([y, x, -1])
            visited[y][x] = 1
            cnt += 1
day = 0

while Q:
    y, x, d = Q.popleft()
    if d > day:
        day = d
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < N and 0 <= nx < M:
            if visited[ny][nx] == 0 and box[ny][nx] == 0:
                visited[ny][nx] = 1
                box[ny][nx] = 1
                Q.append([ny, nx, d + 1])
                cnt += 1

if cnt == max_cnt:
    if day == 0:
        print(0)
    else:
        print(day + 1)
else:
    print(-1)

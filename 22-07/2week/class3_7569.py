# 7569. 토마토
# Level Gold5
# Link : https://www.acmicpc.net/problem/7569

import sys
from collections import deque

dh = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 0, 1, 0]
dx = [0, 0, 0, 1, 0, -1]

M, N, H = map(int, sys.stdin.readline().split())

brd = []
for _ in range(H):
    tmp = [sys.stdin.readline().split() for _ in range(N)]
    brd.append(tmp)

q = deque()
for h in range(H):
    for y in range(N):
        for x in range(M):
            if brd[h][y][x] == '1':
                q.append([h, y, x, 0])
cnt = 0
while q:
    rh, ry, rx, cnt = q.popleft()
    for i in range(6):
        nh = rh + dh[i]
        ny = ry + dy[i]
        nx = rx + dx[i]
        if 0 <= nh < H and 0 <= ny < N and 0 <= nx < M and brd[nh][ny][nx] == '0':
            brd[nh][ny][nx] = '1'
            q.append([nh, ny, nx, cnt + 1])

completed = True
for h in range(H):
    if not completed:
        break
    for y in range(N):
        if not completed:
            break
        for x in range(M):
            if brd[h][y][x] == '0':
                print(-1)
                completed = False
                break
if completed:
    print(cnt)

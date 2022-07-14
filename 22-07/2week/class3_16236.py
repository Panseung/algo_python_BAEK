# 16236. 아기 상어
# Level Gold3
# Link : https://www.acmicpc.net/problem/16236

import sys
from collections import deque

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


def find_prey():
    global prey_lst
    lst = []
    for i in range(N):
        for j in range(N):
            if 0 < sea[i][j] < size:
                lst.append([i, j])
    prey_lst = lst
    return


def cal_distance(py, px, time):
    q = deque()
    q.append([y, x, time])
    visited = [[0] * N for _ in range(N)]
    while q:
        a, b, t = q.popleft()
        for i in range(4):
            ny = a + dy[i]
            nx = b + dx[i]
            if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx] and sea[ny][nx] <= size:
                visited[ny][nx] = 1
                q.append([ny, nx, t + 1])
                if ny == py and nx == px:
                    return t + 1, py, px


N = int(sys.stdin.readline())
y, x = 0, 0
sea = []
for i in range(N):
    tmp = list(map(int, sys.stdin.readline().split()))
    for j in range(N):
        if tmp[j] == 9:
            y, x = i, j
            tmp[j] = 0
    sea.append(tmp)

answer = 0
size = 2
eat_cnt = 0
prey_lst = []
find_prey()
while prey_lst:
    min_distance = 1e9
    new_y, new_x = 0, 0
    changed = False
    for pos in prey_lst:
        res = cal_distance(pos[0], pos[1], 0)
        if not res:
            continue
        dis, ty, tx = res[0], res[1], res[2]
        if dis < min_distance:
            min_distance, new_y, new_x = dis, ty, tx
            changed = True
    if not changed:
        break
    y, x = new_y, new_x
    sea[y][x] = 0
    answer += min_distance
    eat_cnt += 1
    if size == eat_cnt:
        size += 1
        eat_cnt = 0
    find_prey()

print(answer)


# 10026. 적록색약
# Level Gold5
# Link : https://www.acmicpc.net/problem/10026


from collections import deque

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

N = int(input())
brd = list()
for _ in range(N):
    tmp = list()
    S = input()
    for s in S:
        tmp.append(s)
    brd.append(tmp)
visited1 = [[0] * N for _ in range(N)]
visited2 = [[0] * N for _ in range(N)]
answer1 = 0
answer2 = 0

for y in range(N):
    for x in range(N):
        if not visited1[y][x]:
            visited1[y][x] = 1
            q = deque()
            q.append([y, x])
            color = brd[y][x]
            answer1 += 1
            while q:
                ry, rx = q.popleft()
                for i in range(4):
                    ny = ry + dy[i]
                    nx = rx + dx[i]
                    if 0 <= ny < N and 0 <= nx < N and not visited1[ny][nx] and brd[ny][nx] == color:
                        visited1[ny][nx] = 1
                        q.append([ny, nx])
        if not visited2[y][x]:
            visited2[y][x] = 1
            q = deque()
            q.append([y, x])
            color = brd[y][x]
            if color != 'B':
                color = 'RG'
            answer2 += 1
            while q:
                ry, rx = q.popleft()
                for i in range(4):
                    ny = ry + dy[i]
                    nx = rx + dx[i]
                    if 0 <= ny < N and 0 <= nx < N and not visited2[ny][nx] and brd[ny][nx] in color:
                        visited2[ny][nx] = 1
                        q.append([ny, nx])
print(answer1, answer2)

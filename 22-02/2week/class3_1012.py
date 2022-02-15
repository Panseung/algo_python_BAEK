# 1012. 유기농 배추
# Level Silver2
# Link : https://www.acmicpc.net/problem/1012

import sys

sys.setrecursionlimit(10 ** 6)
my_input = sys.stdin.readline

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def worm(pos_y, pos_x):
    for i in range(4):
        new_y = pos_y + dy[i]
        new_x = pos_x + dx[i]
        if 0 <= new_y < N and 0 <= new_x < M and not visited[new_y][new_x] and field[new_y][new_x]:
            visited[new_y][new_x] = 1
            worm(new_y, new_x)


T = int(my_input())
for tc in range(T):
    M, N, K = map(int, my_input().split())
    field = [[0] * M for _ in range(N)]
    for _ in range(K):
        x, y = map(int, my_input().split())
        field[y][x] = 1
    visited = [[0] * M for _ in range(N)]
    result = 0
    for y in range(N):
        for x in range(M):
            if field[y][x] == 1 and visited[y][x] == 0:
                result += 1
                visited[y][x] = 1
                worm(y, x)
    print(result)

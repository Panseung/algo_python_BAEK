# 14500. 테트로미노
# Level Gold5
# Link : https://www.acmicpc.net/problem/14500

import sys


def solve(y, x):
    global answer
    max_v = 0
    if 0 <= y < N - 3:  # ㅣ
        tmp = 0
        for i in range(4):
            tmp += brd[y + i][x]
        if tmp > max_v:
            max_v = tmp

    if 0 <= x < M - 3:  # ㅡ
        tmp = 0
        for i in range(4):
            tmp += brd[y][x + i]
        if tmp > max_v:
            max_v = tmp

    if 0 <= y < N - 1 and 0 <= x < M - 1:  # 네모
        tmp = 0
        for i in range(2):
            for j in range(2):
                tmp += brd[y + i][x + j]
        if tmp > max_v:
            max_v = tmp

    if 0 <= y < N - 1 and 0 <= x < M - 2:  # ㄱ자 누웠을 때, ㄹ자 누웠을 때
        tmp = 0
        for i in range(3):  # ㄱ자 두개
            tmp += brd[y][x + i]
        tmp += max(brd[y + 1][x], brd[y + 1][x + 2])
        if tmp > max_v:
            max_v = tmp

        tmp = 0
        for i in range(3):  # ㄴ자 두개
            tmp += brd[y + 1][x + i]
        tmp += max(brd[y][x], brd[y][x + 2])
        if tmp > max_v:
            max_v = tmp

        tmp = 0
        for i in range(2):  # ㄹ자 두개
            tmp += brd[y + i][x + 1]
        tmp += max(brd[y][x] + brd[y + 1][x + 2], brd[y][x + 2] + brd[y + 1][x])
        if tmp > max_v:
            max_v = tmp

    if 0 <= y < N - 2 and 0 <= x < M - 1:  # ㄴ자 섰을 때, ㄹ자 섰을 때
        tmp = 0
        for i in range(3):  # ㄴ
            tmp += brd[y + i][x]
        tmp += max(brd[y][x + 1], brd[y + 2][x + 1])
        if tmp > max_v:
            max_v = tmp

        tmp = 0
        for i in range(3):  # ㄱ
            tmp += brd[y + i][x + 1]
        tmp += max(brd[y][x], brd[y + 2][x])
        if tmp > max_v:
            max_v = tmp

        tmp = 0
        for i in range(2):
            tmp += brd[y + 1][x + i]
        tmp += max(brd[y][x] + brd[y + 2][x + 1], brd[y][x + 1] + brd[y + 2][x])
        if tmp > max_v:
            max_v = tmp
    if 0 <= y < N - 1 and 0 <= x < M - 2:  # ㅗ, ㅜ
        tmp = 0
        for i in range(3):  # ㅜ
            tmp += brd[y][x + i]
        tmp += brd[y + 1][x + 1]
        if tmp > max_v:
            max_v = tmp

        tmp = 0
        for i in range(3):  # ㅗ
            tmp += brd[y + 1][x + i]
        tmp += brd[y][x + 1]
        if tmp > max_v:
            max_v = tmp

    if 0 <= y < N - 2 and 0 <= x < M - 1:  # ㅓ, ㅏ
        tmp = 0
        for i in range(3):  # ㅏ
            tmp += brd[y + i][x]
        tmp += brd[y + 1][x + 1]
        if tmp > max_v:
            max_v = tmp

        tmp = 0
        for i in range(3):  # ㅓ
            tmp += brd[y + i][x + 1]
        tmp += brd[y + 1][x]
        if tmp > max_v:
            max_v = tmp

    if max_v > answer:
        answer = max_v
    return


N, M = map(int, sys.stdin.readline().split())

brd = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
answer = 0

for i in range(N):
    for j in range(M):
        solve(i, j)
print(answer)

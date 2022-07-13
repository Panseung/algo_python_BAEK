# 1992. 쿼드트리
# Level Silver1
# Link : https://www.acmicpc.net/problem/1992

import sys


def solve(y, x, l):
    global answer
    nl = l // 2
    bw = video[y][x]
    for i in range(y, y + l):
        for j in range(x, x + l):
            if video[i][j] != bw:
                answer += '('
                for ry in range(y, y + l, nl):
                    for rx in range(x, x + l, nl):
                        solve(ry, rx, nl)
                answer += ')'
                return
    if bw == '1':
        answer += '1'
    else:
        answer += '0'


N = int(input())
video = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
answer = ''
solve(0, 0, N)
print(answer)

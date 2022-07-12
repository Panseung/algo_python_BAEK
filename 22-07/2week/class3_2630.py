# 2630. 색종이 만들기
# Level Silver2
# Link : https://www.acmicpc.net/problem/2630


import sys

def solve(x, y, length):
    num = paper[y][x]
    next_len = length // 2
    for ry in range(y, y + length):
        for rx in range(x, x + length):
            if paper[ry][rx] != num:
                for i in range(2):
                    for j in range(2):
                        solve(x + i * next_len, y + j * next_len, next_len)
                return
    answer[num] += 1


N = int(input())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
answer = [0, 0]
solve(0, 0, N)
for a in answer:
    print(a)

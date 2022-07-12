# 1931. 회의실 배정
# Level Silver1
# Link : https://www.acmicpc.net/problem/1931

import sys

N = int(input())
schedules = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
schedules.sort(key=lambda x: (x[1], x[0]))
time = 0
answer = 0
for s in schedules:
    start, end = s
    if start >= time:
        answer += 1
        time = end

print(answer)

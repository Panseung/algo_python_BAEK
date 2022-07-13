# 2667. 단지번호붙이기
# Level Silver1
# Link : https://www.acmicpc.net/problem/2667


import sys

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


N = int(input())
house = [list(sys.stdin.readline().rstrip()) for _ in range(N)]

answer = 0
answer_lst = []
visited = [[0] * N for _ in range(N)]
for y in range(N):
    for x in range(N):
        if house[y][x] == '1' and not visited[y][x]:
            visited[y][x] = 1
            answer += 1
            cnt = 1
            stack = [[y, x]]
            while stack:
                ry, rx = stack.pop()
                for i in range(4):
                    ny = ry + dy[i]
                    nx = rx + dx[i]
                    if 0 <= ny < N and 0 <= nx < N and house[ny][nx] == '1' and not visited[ny][nx]:
                        stack.append([ny, nx])
                        visited[ny][nx] = 1
                        cnt += 1
            answer_lst.append(cnt)

print(answer)
answer_lst.sort()
for a in answer_lst:
    print(a)



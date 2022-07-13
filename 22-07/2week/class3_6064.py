# 6064. 카잉 달력
# Level Silver1
# Link : https://www.acmicpc.net/problem/6064


T = int(input())
for _ in range(T):
    m, n, x, y = map(int, input().split())
    answer = x
    ny, nx = x, x
    while ny > n:
        ny -= n
    visited = [0] * (n + 1)
    visited[ny] = 1
    if y == ny or n == 1:
        print(answer)
    else:
        while True:
            answer += m
            ny = ny + m
            while ny > n:
                ny -= n

            if ny == y:
                print(answer)
                break

            if visited[ny]:
                print(-1)
                break

            visited[ny] = 1

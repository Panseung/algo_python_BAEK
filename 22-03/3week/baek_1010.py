# 1010. 다리 놓기
# Level Silver4
# Link : https://www.acmicpc.net/problem/1010

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())

    left = 1
    for i in range(N):
        left *= M - i

    right = 1
    for i in range(1, N + 1):
        right *= i

    print(left // right)

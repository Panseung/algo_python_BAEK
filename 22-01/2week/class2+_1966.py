# 1966. 프린터 큐
# Level Silver3
# Link : https://www.acmicpc.net/problem/1966

from collections import deque

TC = int(input())
for tc in range(TC):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    num_originPos = deque()

    for i in range(N):
        num_originPos.append([lst[i], i])

    turn = 0
    found = False
    importantV = max(num_originPos)[0]
    while not found:
        V, pos = num_originPos.popleft()
        if V == importantV:
            turn += 1
            if pos == M:
                found = True
            else:
                importantV = max(num_originPos)[0]
        else:
            num_originPos.append([V, pos])

    print(turn)

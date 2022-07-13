# 2579. 계단 오르기
# Level Silver3
# Link : https://www.acmicpc.net/problem/2579


import sys

N = int(input())
steps = [0]
for _ in range(N):
    steps.append(int(sys.stdin.readline().rstrip()))
if N == 1:
    print(steps[1])
elif N == 2:
    print(steps[1] + steps[2])
else:
    result = [0] * (N + 1)
    result[1] = steps[1]
    result[2] = steps[1] + steps[2]
    idx = 2
    while idx < N:
        idx += 1
        result[idx] = max(result[idx - 2] + steps[idx], result[idx - 3] + steps[idx - 1] + steps[idx])

    print(result[N])

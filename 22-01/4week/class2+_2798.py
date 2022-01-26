# 2798. 블랙잭
# Level Bronze2
# Link : https://www.acmicpc.net/problem/2798


N, M = map(int, input().split())

cards = list(map(int, input().split()))

result = 0
for i in range(N - 2):
    for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
            sumV = cards[i] + cards[j] + cards[k]
            if sumV > M:
                continue
            elif sumV > result:
                result = sumV
print(result)

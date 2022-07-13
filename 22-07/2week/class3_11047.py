# 11047. 동전 0
# Level Silver4
# Link : https://www.acmicpc.net/problem/11047


N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]
answer = 0
coins.reverse()
for coin in coins:
    if K >= coin:
        answer += K // coin
        K %= coin
print(answer)


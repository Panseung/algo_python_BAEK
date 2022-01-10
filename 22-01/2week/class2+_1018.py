# 1018. 체스판 다시 칠하기
# Level Silver5
# Link : https://www.acmicpc.net/problem/1018

N, M = map(int, input().split())

BRD = list()

for n in range(N):
    BRD.append(input())

W_change_result = 64
B_change_result = 64

for i in range(N - 7):
    for j in range(M - 7):
        start_W_change = 0
        start_B_change = 0
        for y in range(8):
            for x in range(8):
                if y % 2 == x % 2:
                    if BRD[y + i][x + j] == 'W':
                        start_B_change += 1
                    else:
                        start_W_change += 1
                else:
                    if BRD[y + i][x + j] == 'W':
                        start_W_change += 1
                    else:
                        start_B_change += 1
        if start_W_change < W_change_result:
            W_change_result = start_W_change
        if start_B_change < B_change_result:
            B_change_result = start_B_change

print(min(W_change_result, B_change_result))

# 2839. 설탕 배달
# Level Bronze1
# Link : https://www.acmicpc.net/problem/2839

N = int(input())

cnt_5 = 0
cnt_3 = 0
weight = 0
while weight < N:
    cnt_5 += 1
    weight += 5

while weight != N and cnt_5 > 0:
    if weight > N:
        cnt_5 -= 1
        cnt_3 += 1
        weight -= 2
    if weight < N:
        cnt_3 += 1
        weight += 3


if weight == N:
    print(cnt_5 + cnt_3)
else:
    print(-1)

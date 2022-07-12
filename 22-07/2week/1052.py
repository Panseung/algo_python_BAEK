# 1052. 물병
# Level Silver1
# Link : https://www.acmicpc.net/problem/1052


N, K = map(int, input().split())
bottles = [0] * 27

result = 0
answer = 0
for i in range(27, 0, -1):
    if N >= 2 ** i:
        bottles[i] = N // 2 ** i
        N = N - bottles[i] * 2 ** i
bottles[0] = N

cnt = sum(bottles)
while cnt > K:
    changed = False
    for i in range(27):
        if bottles[i]:
            result += 2 ** i
            bottles[i] = 2
            break

    for i in range(27):
        if bottles[i] == 2:
            bottles[i + 1] += 1
            bottles[i] = 0
    cnt = sum(bottles)
print(result)

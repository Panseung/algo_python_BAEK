# 1929. 소수 구하기
# Level Silver2
# Link : https://www.acmicpc.net/problem/1929

M, N = map(int, input().split())
num_lst = [0] * (N + 1)
num_lst[0] = 1
num_lst[1] = 1
prime_lst = list()

res_num = 1

while res_num < N:
    res_num += 1
    if num_lst[res_num]:
        continue
    if res_num >= M:
        prime_lst.append(res_num)
    for i in range(res_num, N + 1, res_num):
        num_lst[i] = 1

print(*prime_lst, sep='\n')

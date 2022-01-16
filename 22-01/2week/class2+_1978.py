# 1978. 소수 찾기
# Level Silver4
# Link : https://www.acmicpc.net/problem/1978

N = int(input())
lst = list(map(int, input().split()))
max_num = max(lst)
num_lst = [0] * (max_num + 1)
num_lst[0] = 1
num_lst[1] = 1

res_num = 1
while res_num < max_num:
    res_num += 1
    if num_lst[res_num]:
        continue
    for i in range(res_num * 2, max_num + 1, res_num):
        num_lst[i] = 1

result = 0
for i in lst:
    if num_lst[i] == 0:
        result += 1

print(result)
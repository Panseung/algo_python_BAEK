# 2231. 분해합
# Level Bronze2
# Link : https://www.acmicpc.net/problem/2231

N = int(input())
num = N - 9 * len(str(N))
result = 0

while num < N:
    str_num = str(num)
    result_num = num
    for n in str_num:
        if n == '-':
            continue
        result_num += int(n)

    if result_num == N:
        result = num
        break
    else:
        num += 1

print(result)

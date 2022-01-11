# 1436. 영화감독 숌
# Level Silver5
# Link : https://www.acmicpc.net/problem/1436

devil_nums = [0, 666]

num = int(input()) + 1

res_num = 666
while len(devil_nums) < num:
    res_num += 1
    test_num = str(res_num)
    for i in range(len(test_num) - 2):
        if test_num[i:i + 3] == '666':
            devil_nums.append(res_num)
            break

print(devil_nums[-1])

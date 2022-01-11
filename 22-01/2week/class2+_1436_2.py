# 1436. 영화감독 숌
# Level Silver5
# Link : https://www.acmicpc.net/problem/1436

N = int(input())

if N == 1:
    print('666')
else:
    devil_num_cnt = 1

    for i in range(1, N):
        devil_num = '{0}666'.format(i)
        big_six_cnt = 0
        for j in range(-4, -(len(devil_num)) - 1):
            if devil_num[j] == '6':
                big_six_cnt += 1
            else:
                break
        if big_six_cnt:
            devil_num_cnt += 10 ** big_six_cnt
        else:
            devil_num_cnt += 1

        if devil_num_cnt >= N:

            if big_six_cnt:
                devil_num = int(devil_num)
                devil_num += (N - devil_num_cnt)
            print(devil_num)
            break

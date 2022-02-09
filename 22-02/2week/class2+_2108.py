# 2108. 통계학
# Level Silver4
# Link : https://www.acmicpc.net/problem/2108
import sys

my_input = sys.stdin.readline
N = int(my_input())
lst = list()
for _ in range(N):
    lst.append(int(my_input()))
lst.sort()

mode_lst = []
pos = 0
mode_cnt = 0
while pos < N:
    num = lst[pos]
    cnt = 0
    for i in range(pos, N):
        if lst[i] != num:
            break
        pos += 1
        cnt += 1
    if cnt > mode_cnt:
        mode_lst = [[cnt, num]]
        mode_cnt = cnt
    elif cnt == mode_cnt:
        mode_lst.append([cnt, num])

mode_lst.sort()
mode = mode_lst[min(1, len(mode_lst) - 1)][1]

print(round(sum(lst) / N))
print(lst[N // 2])
print(mode)
print(max(lst) - min(lst))

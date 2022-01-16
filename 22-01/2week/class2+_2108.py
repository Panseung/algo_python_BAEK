# 2108. 통계학
# Level Silver4
# Link : https://www.acmicpc.net/problem/2108

N = int(input())
lst = list()
for _ in range(N):
    lst.append(int(input()))
lst.sort()
num_cnt = len(set(lst))
num_freq = [0] * num_cnt

pos = 0
freq_pos = 0
num = lst[0]
while freq_pos < num_cnt and pos < N:
    if lst[pos] == num:
        num_freq[freq_pos] += 1
        pos += 1
    else:
        freq_pos += 1
        num = lst[pos]

max_freq = max(num_freq)
max_freq_idx = list()
for i in range(num_cnt):
    if num_freq[i] == max_freq:
        max_freq_idx.append(i)

set_lst = list(set(lst))
set_lst.sort()
mode_idx = max_freq_idx[min(1, len(max_freq_idx) - 1)]
print(set_lst)
print(max_freq_idx)
print(mode_idx)


print(round(sum(lst) / N))
print(lst[N // 2])
print(max(lst) - min(lst))

# 18870. 좌표 압축
# Level Silver2
# Link : https://www.acmicpc.net/problem/18870

import sys

my_input = sys.stdin.readline

N = int(my_input())
lst = list(map(int, my_input().split()))

set_lst = list(sorted(set(lst)))

dic = {set_lst[i]: i for i in range(len(set_lst))}

for i in lst:
    print(dic[i], end=' ')

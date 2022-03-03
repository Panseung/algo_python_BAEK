# 1620. 나는야 포켓몬 마스터
# Level Silver4
# Link : https://www.acmicpc.net/problem/1620

import sys

my_input = sys.stdin.readline

N, M = map(int, my_input().split())

dic = dict()

for i in range(1, N + 1):
    s = my_input().rstrip()
    dic[i] = s
    dic[s] = i

for _ in range(M):
    quest = my_input().rstrip()
    if quest.isdigit():
        print(dic[int(quest)])
    else:
        print(dic[quest])

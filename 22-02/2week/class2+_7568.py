# 7568. 덩치
# Level Silver5
# Link : https://www.acmicpc.net/problem/7568

import sys

my_input = sys.stdin.readline

people = list()
N = int(my_input())
for i in range(N):
    weight, height = map(int, my_input().split())
    people.append([weight,height])

for i in people:
    cnt = 1
    for j in people:
        if i[0] < j[0] and i[1] < j[1]:
            cnt += 1
    print(cnt, end=" ")


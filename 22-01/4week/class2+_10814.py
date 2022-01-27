# 10814. 나이순 정렬
# Level Silver5
# Link : https://www.acmicpc.net/problem/10814

import sys

users = [[] for _ in range(201)]

for _ in range(int(sys.stdin.readline())):
    age, name = sys.stdin.readline().split()
    users[int(age)].append(name)

for i in range(201):
    if users[i]:
        for user in users[i]:
            print(i, user)

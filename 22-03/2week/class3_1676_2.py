# 1676. 팩토리얼 0의 개수
# Level Silver4
# Link : https://www.acmicpc.net/problem/1676

import sys

my_input = sys.stdin.readline

N = int(my_input())

result = 1
for i in range(1, N + 1):
    result *= i

num = 10
cnt = 0
while result % num == 0:
    cnt += 1
    num *= 10

print(cnt)

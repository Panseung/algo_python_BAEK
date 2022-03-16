# 11399. ATM
# Level Silver3
# Link : https://www.acmicpc.net/problem/11399


import sys

my_input = sys.stdin.readline

N = int(my_input())
lst = list(map(int, my_input().split()))

lst.sort()
result = 0
tmp = 0
for i in lst:
    tmp += i
    result += tmp
print(result)

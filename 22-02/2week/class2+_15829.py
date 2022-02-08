# 15829. Hashing
# Level Bronze2
# Link : https://www.acmicpc.net/problem/15829

import sys

my_input = sys.stdin.readline

L = int(my_input())
word = my_input().rstrip()
values = list()
for alpha in word:
    values.append(ord(alpha) - 96)

result = 0
for i in range(L):
    result += values[i] * 31 ** i
print(result % 1234567891)

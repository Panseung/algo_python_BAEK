# 2908. 상수
# Level Bronze2
# Link : https://www.acmicpc.net/problem/2577

import sys

my_input = sys.stdin.readline

num1, num2 = my_input().split()

num1 = int(num1[::-1])
num2 = int(num2[::-1])

print(max(num1, num2))

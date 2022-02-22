# 11720. 숫자의 합
# Level Bronze2
# Link : https://www.acmicpc.net/problem/2577

import sys

my_input = sys.stdin.readline

N = int(my_input())
number = my_input().rstrip()

result = 0
for num in number:
    result += int(num)

print(result)

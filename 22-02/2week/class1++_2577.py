# 2577. 숫자의 갯수
# Level Bronze2
# Link : https://www.acmicpc.net/problem/2577

import sys

my_input = sys.stdin.readline

nums = [0] * 10
num = 1
for _ in range(3):
    num *= int(my_input().rstrip())

num = str(num)

for i in num:
    nums[int(i)] += 1

for result in nums:
    print(result)

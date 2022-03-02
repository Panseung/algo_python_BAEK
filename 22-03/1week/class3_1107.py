# 1107. 리모컨
# Level Gold 5
# Link : https://www.acmicpc.net/problem/1107

import sys

my_input = sys.stdin.readline

N = int(my_input().rstrip())
M = int(my_input())
result = abs(100 - int(N))
if M:
    broken_btn = list(map(int, my_input().split()))
else:
    broken_btn = list()

for num in range(1000001):
    for n in str(num):
        if int(n) in broken_btn:
            break
    else:
        result = min(result, len(str(num)) + abs(num - N))
print(result)

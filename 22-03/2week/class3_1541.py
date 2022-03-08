# 1541. 잃어버린 괄호
# Level Silver2
# Link : https://www.acmicpc.net/problem/1541

import sys

my_input = sys.stdin.readline

S = my_input()

result = 0

direct = True

tmp = ''

for s in S:
    if s == '+' or s == '-':
        if direct:
            result += int(tmp)
        else:
            result -= int(tmp)
        if s == '-':
            direct = False
        tmp = ''
    else:
        tmp += s
if direct:
    result += int(tmp)
else:
    result -= int(tmp)


print(result)

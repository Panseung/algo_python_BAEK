# 4949. 균형잡힌 세상
# Level Silver4
# Link : https://www.acmicpc.net/problem/4949

import sys

my_input = sys.stdin.readline

while True:
    line = my_input().rstrip()
    if line == '.':
        break

    result = 'yes'
    stack = list()
    for word in line:
        if word == '(' or word == '[':
            stack.append(word)
        elif word == ')':
            if stack:
                if stack[-1] == '(':
                    stack.pop()
                else:
                    result = 'no'
                    break
            else:
                result = 'no'
                break
        elif word == ']':
            if stack:
                if stack[-1] == '[':
                    stack.pop()
                else:
                    result = 'no'
                    break
            else:
                result = 'no'
                break
    if stack:
        result = 'no'
    print(result)

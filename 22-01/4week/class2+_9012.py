# 9012. 괄호
# Level Silver4
# Link : https://www.acmicpc.net/problem/9012

TC = int(input())
for tc in range(TC):
    parens = list(input())
    stack = list()
    result = 'YES'
    for par in parens:
        if par == '(':
            stack.append(par)
        else:
            if stack:
                stack.pop()
            else:
                result = 'NO'
                break
    if stack:
        result = 'NO'
    print(result)
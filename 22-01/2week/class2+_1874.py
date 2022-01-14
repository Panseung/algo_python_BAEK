# 1874. 스택 수열
# Level Silver3
# Link : https://www.acmicpc.net/problem/1874

n = int(input())
num_lst = list()
for i in range(n):
    num_lst.append(int(input()))

num = 1
stack = list()
result = list()
need_num_idx = 0
enable = True
while need_num_idx < n:
    need_num = num_lst[need_num_idx]

    if stack and stack[-1] == need_num:
        stack.pop()
        result.append('-')
        need_num_idx += 1
    else:
        stack.append(num)
        result.append('+')
        num += 1
    if num > n + 1:
        enable = False
        break
if enable:
    print(*result, sep='\n')
else:
    print('NO')

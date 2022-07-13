# 9019. DSLR
# Level Gold4
# Link : https://www.acmicpc.net/problem/9019
# pypy3 제출

from collections import deque

d = ['D', 'S', 'L', 'R']


def solve(cmd, number):
    r_num = number
    if cmd == 'D':
        r_num *= 2
        if r_num >= 10000:
            r_num -= 10000

    elif cmd == 'S':
        r_num -= 1
        if r_num < 0:
            r_num = 9999
    elif cmd == 'L':
        tmp_num = r_num // 1000
        r_num %= 1000
        r_num *= 10
        r_num += tmp_num
    else:
        tmp_num = r_num % 10
        r_num //= 10
        r_num += tmp_num * 1000
    return r_num


T = int(input())
for _ in range(T):
    A, B = map(int, input().split())

    visit = [0] * 10000
    q = deque()
    q.append(['', A])
    while q:
        result, num = q.popleft()
        if num == B:
            print(result)
            break

        for i in range(4):
            res = solve(d[i], num)
            if not visit[int(res)]:
                visit[int(res)] = 1
                q.append([result + d[i], res])

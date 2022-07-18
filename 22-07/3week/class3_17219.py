# 17219. 비밀번호 찾기
# Level Silver4
# Link : https://www.acmicpc.net/problem/17219

import sys

N, M = map(int, sys.stdin.readline().split())

dic = dict(sys.stdin.readline().rstrip().split() for _ in range(N))

for _ in range(M):
    print(dic[sys.stdin.readline().rstrip()])

# import sys
#
# N, M = map(int, sys.stdin.readline().split())
#
# sites = [[] for _ in range(58)]
# passwords = [[] for _ in range(58)]
#
# for _ in range(N):
#     s, p = sys.stdin.readline().split()
#     idx = ord(s[0])
#     idx -= 65
#     sites[idx].append(s)
#     passwords[idx].append(p)
#
# for _ in range(M):
#     s = sys.stdin.readline().rstrip()
#     idx = ord(s[0])
#     idx -= 65
#     for i in range(len(sites[idx])):
#         if s == sites[idx][i]:
#             print(passwords[idx][i])
#             break


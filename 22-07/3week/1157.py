# 1157. 단어 공부
# Level Bronze1
# Link : https://www.acmicpc.net/problem/1157

import sys

word = sys.stdin.readline().rstrip().lower()

word_set = list(set(word))
cnt = 0
question = False
answer = ''
for w in word_set:
    res_cnt = word.count(w)
    if res_cnt > cnt:
        question = False
        cnt = res_cnt
        answer = w.upper()
    elif res_cnt == cnt:
        question = True

if question:
    print('?')
else:
    print(answer)

# S = sys.stdin.readline().rstrip()
#
# dic = dict()
# for i in range(ord('a'), ord('z') + 1):
#     dic[chr(i)] = 0
#
# for s in S:
#     dic[s.lower()] += 1
#
# max_cnt = 0
# question = False
# answer = ''
# for d, v in dic.items():
#     if v > max_cnt:
#         max_cnt = v
#         answer = d.upper()
#         question = False
#     elif v == max_cnt:
#         question = True
# if question:
#     print('?')
# else:
#     print(answer)

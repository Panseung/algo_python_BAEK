# 1157. 단어 공부
# Level Bronze1
# Link : https://www.acmicpc.net/problem/1157

import sys

my_input = sys.stdin.readline

word = my_input().lower()

word_set = list(set(word))

result = list()

for alpha in word_set:
    cnt = word.count(alpha)
    result.append(cnt)

maxV = max(result)
max_cnt = 0
for i in range(len(result)):
    if result[i] == maxV:
        max_cnt += 1
if max_cnt >= 2:
    print("?")
else:
    idx = 0
    for j in range(len(result)):
        if result[j] == maxV:
            idx = j
            break
    print(word_set[j].upper())

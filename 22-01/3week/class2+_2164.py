# 2164. 카드2
# Level Silver4
# Link : https://www.acmicpc.net/problem/2164

from collections import deque

N = int(input())
card_lst = deque()
for i in range(1, N + 1):
    card_lst.append(i)

while len(card_lst) > 1:
    card_lst.popleft()
    card_lst.append(card_lst.popleft())

print(card_lst[0])
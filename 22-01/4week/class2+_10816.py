# 10816. 숫자 카드 2
# Level Silver4
# Link : https://www.acmicpc.net/problem/10816

import sys

my_input = sys.stdin.readline

N = int(my_input())
cards = list(map(int, my_input().split()))
cards.sort()
M = int(my_input())
result_cards = list(map(int, my_input().split()))
minV, maxV = min(result_cards), max(result_cards)

new_cards = list()
for card in cards:
    if minV <= card <= maxV:
        new_cards.append(card)

for card in result_cards:
    cnt = 0
    for card2 in new_cards:
        if card == card2:
            cnt += 1
        elif card < card2:
            break
    print(cnt, end=' ')

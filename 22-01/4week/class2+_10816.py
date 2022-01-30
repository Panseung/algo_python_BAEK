# 10816. 숫자 카드 2
# Level Silver4
# Link : https://www.acmicpc.net/problem/10816

import sys

my_input = sys.stdin.readline

N = int(my_input())
cards = list(map(int, my_input().split()))
M = int(my_input())
result_cards = list(map(int, my_input().split()))

cards_set = list(set(cards + result_cards))
dic = dict()
for card in cards_set:
    dic[card] = 0
for card in cards:
    dic[card] += 1
for card in result_cards:
    print(dic[card], end=' ')
